import 'package:flutter/material.dart';

class DefaultHomeWidget extends StatelessWidget {
  const DefaultHomeWidget({super.key});

  @override
  Widget build(BuildContext context) {
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
              },
              icon: const Icon(Icons.wifi_protected_setup),
              label: const Text("Write debug Test!")),
        ]));
  }
}
