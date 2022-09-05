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
    final testingChild = db.child('v1/testing/1');
    final DatabaseReference streamChild = db.child('v1/stream/json');

    return Padding(
      padding: const EdgeInsets.all(12.0),
      //   child: Column(crossAxisAlignment: CrossAxisAlignment.center, children: [
      //     const Text("Yay!"),
      //     SizedBox(
      //       height: 10,
      //       width: MediaQuery.of(context).size.width,
      //     ),
      //     ElevatedButton.icon(
      //         onPressed: () {
      //           debugPrint("Debug Read pressed");
      //         },
      //         icon: const Icon(Icons.read_more),
      //         label: const Text("Read debug Test!")),
      //     ElevatedButton.icon(
      //         onPressed: () {
      //           debugPrint("Debug Write pressed");
      //           testingChild.set(
      //             {"time": DateTime.now().millisecondsSinceEpoch},
      //           );
      //         },
      //         icon: const Icon(Icons.wifi_protected_setup),
      //         label: const Text("Write debug Test!")),
      // ]
      child: InteractiveViewer(
        boundaryMargin: const EdgeInsets.all(10.0),
        minScale: 0.01,
        maxScale: 2000,
        child: StreamBuilder(
          stream: streamChild.onValue,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              final data = snapshot.data!
                  as DatabaseEvent; // Fails if there is no data stored
              final String rawJson = data.snapshot.value
                  as String; // Fails if the data is not simply a string
              final List<dynamic> rawData = jsonDecode(rawJson)
                  as List<dynamic>; // Fails if the data is not valid JSON
              final List<int> typedData = rawData
                  .map((e) => e as int)
                  .toList(); // Fails if the data is not a list of integers
              assert(rawData.length ==
                  width * height); // Fails if the data is not the correct size
              return GridView.count(crossAxisCount: width, children: [
                for (final int value in typedData)
                  Container(
                    color: Color.fromARGB(10, value * 3, 0, 0),
                    child: Text("$value"),
                  )
              ]);
            } else {
              return const Text("No data");
            }
          },
        ),
      ),
    );
  }
}
