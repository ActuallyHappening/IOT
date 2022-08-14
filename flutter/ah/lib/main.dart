import 'package:ah/routing.dart';
import 'package:flutter/material.dart';

void main() {
  print("Starting ...");
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: MyRouting.initialRoute,
      routes: MyRouting.routes,
    );
  }
}
