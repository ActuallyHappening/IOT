// Minimal reproducible code

import 'package:flutter/material.dart';
import 'package:touch_bar/touch_bar.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  Future<void> doTouchBar() async {
    try {
      await setTouchBar(
          TouchBar(children: [TouchBarLabel('Testing Touch Bar ...')]));
    } catch (e) {
      print(
          "How do I catch this error when on a platform not supporting touch bar? $e");
    }
  }

  @override
  void initState() {
    super.initState();
    doTouchBar();
  }

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Touch Bar Demo',
      home: Center(child: Text('Hello World!')),
    );
  }
}
