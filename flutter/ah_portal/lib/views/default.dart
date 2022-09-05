import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';

class DefaultHomeWidget extends StatelessWidget {
  DefaultHomeWidget({super.key});

  final db = FirebaseDatabase.instance.ref();

  @override
  Widget build(BuildContext context) {
    final testingChild = db.child('v1/testing/1');

    return Padding(
        padding: const EdgeInsets.all(12.0),
        child: Column(crossAxisAlignment: CrossAxisAlignment.center, children: [
          const Text("Yay!"),
          SizedBox(
            height: 10,
            width: MediaQuery.of(context).size.width,
          ),
          ElevatedButton.icon(
              onPressed: () {
                debugPrint("Debug Read pressed");
              },
              icon: const Icon(Icons.read_more),
              label: const Text("Read debug Test!")),
          ElevatedButton.icon(
              onPressed: () {
                debugPrint("Debug Write pressed");
                testingChild.set(
                  {"time": DateTime.now().millisecondsSinceEpoch},
                );
              },
              icon: const Icon(Icons.wifi_protected_setup),
              label: const Text("Write debug Test!")),
        ]));
  }
}
