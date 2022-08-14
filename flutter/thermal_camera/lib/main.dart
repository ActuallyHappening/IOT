import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  static const _title = "Flutter layout tutorial";

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: _title,
      home: Scaffold(
        appBar: AppBar(
          title: const Text(_title),
        ),
        body: Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          const Center(
          child: Text('Hello World'),
          ),
          const Center(child: Text("Yay!")),
          Image.network("https://picsum.photos/250?image=10",
              fit: BoxFit.cover),
          Icon(Icons.alarm, color: Colors.red[600])
        ]),
      ),
    );
  }
}
