import 'dart:io';

import 'package:ah/home.dart';
import 'package:ah/settings.dart';
import 'package:flutter/material.dart';
import 'package:menubar/menubar.dart';
import 'package:touch_bar/touch_bar.dart';

import 'aio_sign_in.dart';

class MyRouting {
  static final Map<String, Widget Function(BuildContext)> routes = {
    '/': (context) => const HomeRoute(),
    '/settings': (context) => const SettingsRoute(),
    '/signin': (context) => const AIOSignInRoute(),
  };
  static const String initialRoute = '/';

  static String toRoute(String name) {
    debugPrint("toRoute: $name");
    return commonRouteNames[commonRouteNames.keys.firstWhere(
        (commonName) => name.toLowerCase() == commonName.toLowerCase(),
        orElse: () => throw Exception('No route found for $name'))] as String;
  }

  static const Map<String, String> commonRouteNames = {
    "Sign In": "/signin",
    "Settings": "/settings",
    "Home": "/",
  };

  final asyncRegisterhighLevelActions = (BuildContext context) async {
    if (Platform.isMacOS) {
      debugPrint(
          "Yay, we're on macOS; registering touch_bar actions and menu items");

      final TouchBar touchBar;
      List<TouchBarItem> touchBarItems = [];

      final NativeSubmenu menu;
      final List<NativeMenuItem> menuItems = [];

      commonRouteNames.forEach((name, route) {
        debugPrint("  $name -> $route");
        touchBarItems.add(TouchBarButton(
          label: name,
          onClick: () {
            Navigator.pushNamed(context, route);
          },
        ));
        menuItems.add(NativeMenuItem(
          label: name,
          onSelected: () {
            Navigator.pushNamed(context, route);
          },
        ));
      });

      touchBar = TouchBar(children: touchBarItems);
      menu = NativeSubmenu(label: "Screens", children: menuItems);

      setTouchBar(touchBar);
      setApplicationMenu([menu]);
    }
  };
}
