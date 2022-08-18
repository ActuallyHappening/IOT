import 'package:ah/routing.dart';
import 'package:flutter/material.dart';

void main() async {
  debugPrint("Starting ...");
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final MyRouting _route = MyRouting(routes: defaultRoutes);

  @override
  void initState() {
    super.initState();
    // _route.registerAsync(context);
  }

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
