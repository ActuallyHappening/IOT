import 'package:ah_portal/views/debug.dart';
import 'package:ah_portal/views/default.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

import 'firebase_options.dart';

Future<void> main() async {
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  _drawer(BuildContext context) => ListView(
        children: [
          const DrawerHeader(
            decoration: BoxDecoration(
              color: Colors.blue,
            ),
            child: Text('Drawer Header'),
          ),
          ListTile(
            title: const Text('To Debug'),
            onTap: () {
              Navigator.of(context).pushNamed('/debug');
            },
          ),
          ListTile(
            title: const Text('Home'),
            onTap: () {
              Navigator.of(context).pushNamed('/');
            },
          ),
        ],
      );

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      routes: <String, WidgetBuilder>{
        '/': (context) => DefaultHomeView(drawer: _drawer(context)),
        '/debug': (context) => DebugView(drawer: _drawer(context)),
      },
    );
  }
}
