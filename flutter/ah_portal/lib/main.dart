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

  WidgetBuilder _makeView(widget) {
    return (BuildContext context) => Scaffold(
          drawer: _drawer(context),
          appBar: AppBar(
            title: const Text('Flutter Demo'),
          ),
          body: widget,
        );
  }

  Widget _drawer(BuildContext context) => Drawer(
        child: ListView(
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
        ),
      );

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: "/debug",
      routes: <String, WidgetBuilder>{
        '/': _makeView(DefaultHomeWidget),
        '/debug': _makeView(DebugWidget),
      },
    );
  }
}
