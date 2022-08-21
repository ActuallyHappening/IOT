import 'package:ah/routing.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

import 'firebase_options.dart';


void main() async {
  debugPrint("Starting ...");
  runApp(const MyApp());
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final MyRouting _routing = MyRouting();

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
      initialRoute: _routing.initialRoute,
      routes: _routing.routes,
    );
  }
}
