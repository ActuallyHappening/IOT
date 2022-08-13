import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';

void main() {
  debugPrint("Running!");
  debugPaintSizeEnabled = true;
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return CupertinoApp(
        title: 'Learning',
        home: Scaffold(
          appBar: AppBar(
            title: const Text('Learning'),
          ),
          body: const Center(
            child: Text('Hello World'),
          ),
        ));
  }
}
