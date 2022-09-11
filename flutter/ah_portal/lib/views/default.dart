import 'dart:convert';

import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';

class DefaultHomeWidget extends StatelessWidget {
  DefaultHomeWidget({super.key});

  final db = FirebaseDatabase.instance.ref();

  static const int width = 32;
  static const int height = 24;

  @override
  Widget build(BuildContext context) {
    final DatabaseReference streamChild = db.child('v1/stream/json');

    return Padding(
      padding: const EdgeInsets.all(10.0),
      child: StreamBuilder(
        stream: streamChild.onValue,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            // try {
            final data = snapshot.data! as DatabaseEvent;
            final String rawJson = data.snapshot.value as String;
            final List<dynamic> rawData = jsonDecode(rawJson) as List<dynamic>;
            assert(rawData.length == width * height); // Fails
            final List<double> typedData = rawData.map((tempSerialized) {
              if (tempSerialized is int) {
                return tempSerialized.toDouble();
              } else if (tempSerialized is double) {
                return tempSerialized;
              } else {
                throw Exception('Invalid data type');
              }
            }).toList();
            const highestPossibleTemp = 50;
            const lowestPossibleTemp = 10;

            // Find temps not higher than highestPossibleTemp and not lower than lowestPossibleTemp
            final List<double> filteredData = typedData
                .where((temp) =>
                    temp <= highestPossibleTemp && temp >= lowestPossibleTemp)
                .toList();

            final highestTemp = filteredData.reduce((a, b) => a > b ? a : b);
            final lowestTemp = filteredData.reduce((a, b) => a < b ? a : b);
            final avgTemp =
                filteredData.reduce((a, b) => a + b) / typedData.length;
            final tempRange = highestTemp - lowestTemp;
            int pixelsGuessed = 0;
            int pixelsDead = 0;
            final tempColors = typedData.asMap().entries.map((tempInfo) {
              final temp = tempInfo.value;
              final index = tempInfo.key;
              final tempNormalized = (temp - lowestTemp) / tempRange;
              if (tempNormalized < 0 || tempNormalized > 1) {
                // This pixel is an outlier pixel / broken
                pixelsGuessed += 1;

                int x = index % width;
                int y = index ~/ width;
                List<double> adjacentPixelValues = [];

                // Since pixel is outlier then take average of surrounding pixels
                if (x != 0) {
                  // If not left edge pixel, add pixel to left
                  adjacentPixelValues.add(typedData[index - 1]);
                }
                if (x != width - 1) {
                  // If not right edge pixel, add pixel to right
                  adjacentPixelValues.add(typedData[index + 1]);
                }
                if (y != 0) {
                  // If not top edge pixel, add pixel above
                  adjacentPixelValues.add(typedData[index - width]);
                }
                if (y != height - 1) {
                  // If not bottom edge pixel, add pixel below
                  adjacentPixelValues.add(typedData[index + width]);
                }

                // Only consider pixels that are not outliers
                final adjacentPixelValuesFiltered = adjacentPixelValues
                    .where((temp) =>
                        temp <= highestPossibleTemp &&
                        temp >= lowestPossibleTemp)
                    .toList();

                // If no adjacent pixels are not outliers, then pixel is dead
                if (adjacentPixelValuesFiltered.isEmpty) {
                  // Dead pixel = Black
                  pixelsDead += 1;
                  return Colors.black;
                }
                final adjacentPixelValuesAvg = adjacentPixelValuesFiltered
                        .reduce((value, element) => value + element) /
                    adjacentPixelValuesFiltered.length;
                final surroundingTempNormalized =
                    (adjacentPixelValuesAvg - lowestTemp) / tempRange;
                
                assert(surroundingTempNormalized >= 0 &&
                    surroundingTempNormalized <= 1);

                if (x == 15 && y == 12) {
                  print("Pixel at 15, 12 is outlier");
                }

                final tempColor = Color.lerp(
                  Colors.green,
                  Colors.red,
                  surroundingTempNormalized,
                )!;
                return tempColor;
              }
              final tempColor = Color.lerp(
                Colors.green,
                Colors.red,
                tempNormalized,
              );
              return tempColor;
            }).toList();

            Widget info = Wrap(
              children: [
                Chip(
                    label: Text(
                        'Highest temp: ${highestTemp.toStringAsFixed(2)}C')),
                Chip(
                    label:
                        Text('Lowest temp: ${lowestTemp.toStringAsFixed(2)}C')),
                Chip(
                    label:
                        Text('Average temp: ${avgTemp.toStringAsFixed(2)}C')),
                Chip(
                    label:
                        Text('Temp range: ${tempRange.toStringAsFixed(2)}C')),
                Chip(
                    label: Text(
                        'Percentage of pixels interpolated: ${((pixelsGuessed / typedData.length) * 100).toStringAsFixed(2)}%')),
                Chip(label: Text('Number of pixels dead: $pixelsDead')),
              ],
            );
            final pixels = GridView.count(
                crossAxisCount: width,
                padding: const EdgeInsets.all(0),
                children: <Widget>[
                  ...tempColors
                      .map((value) => Container(
                            decoration: BoxDecoration(
                              color: value,
                            ),
                          ))
                      .toList()
                ]);
            return Column(
              children: [
                info,
                const SizedBox(height: 20),
                Expanded(child: pixels),
              ],
            );
          } else {
            return const Center(child: Text("No data"));
          }
        },
      ),
    );
  }
}
