import 'package:ah/routing.dart';
import 'package:flutter/material.dart';
import 'package:touch_bar/touch_bar.dart';

void main() async {
  print("Starting ...");
  final TouchBarImage icon =
      await TouchBarImage.loadFrom(path: 'assets/icon.png');
  runApp(MyApp(icon: icon));
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key, required TouchBarImage icon}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    TouchBarPopover popover = TouchBarPopover(
      items: [
        TouchBarButton(
          label: 'Settings',
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => settings_route()),
            );
          },
        ),
        TouchBarButton(
          label: 'About',
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => about_route()),
            );
          },
        ),
      ],
    );
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(primarySwatch: Colors.blue),
      initialRoute: MyRouting.initialRoute,
      routes: MyRouting.routes,
    );
  }
}
