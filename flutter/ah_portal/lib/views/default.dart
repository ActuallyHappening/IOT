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
            final tempColors = typedData.map((temp) {
              final tempNormalized = (temp - lowestTemp) / tempRange;
              if (tempNormalized < 0 || tempNormalized > 1) {
                return Colors.white;
              }
              final tempColor = Color.lerp(
                Colors.red,
                Colors.green,
                tempNormalized,
              );
              return tempColor;
            }).toList();
            return GridView.count(
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
            // } catch (e) {
            //   debugPrint("Error while parsing data stream");
            //   debugPrint(e.toString());
            //   rethrow;
            //   return const Text(
            //       'Error while trying to show you the thermal camera data :( ');
            // }
          } else {
            return const Center(child: Text("No data"));
          }
        },
      ),
    );
  }
}
