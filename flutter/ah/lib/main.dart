import 'package:ah/routing.dart';
import 'package:flutter/material.dart';

void main() async {
  debugPrint("Starting ...");
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  MyApp({super.key});

  final MyRouting _route = MyRouting(routes: defaultRoutes);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(primarySwatch: Colors.blue),
      initialRoute: _route.initialRoute,
      routes: _route.routes,
    );
  }
}
