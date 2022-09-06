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
            final data = snapshot.data!
                as DatabaseEvent; 
            final String rawJson = data.snapshot.value
                as String; 
            final List<dynamic> rawData = jsonDecode(rawJson)
                as List<dynamic>; 
            final List<int> typedData = rawData
                .map((e) => e as int)
                .toList(); 
            assert(rawData.length ==
                width * height); 
            return GridView.count(
                crossAxisCount: width,
                padding: const EdgeInsets.all(0),
                children: [
                  ...typedData
                      .map((value) => Container(
                            decoration: BoxDecoration(
                                color: Color.fromARGB(255, value * 4, 0, 0)),
                          )
              )
                      .toList()
                ]);
          } else {
            return const Center(child: Text("No data"));
          }
        },
      ),
    );
  }
}
