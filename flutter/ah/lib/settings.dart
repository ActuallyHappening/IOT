import 'package:flutter/material.dart';

class settings_route extends StatefulWidget {
  const settings_route({Key? key}) : super(key: key);
  @override
  State<settings_route> createState() => _settings_routeState();
}

class _settings_routeState extends State<settings_route> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Settings'),
      ),
      body: ListView(
        children: const [
          Center(
            child: Text('Settings'),
          ),
        ],
      ),
    );
  }
}
