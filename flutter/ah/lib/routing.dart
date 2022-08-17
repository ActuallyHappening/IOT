import 'dart:io';

import 'package:ah/home.dart';
import 'package:ah/settings.dart';
import 'package:flutter/material.dart';
import 'package:menubar/menubar.dart';
import 'package:touch_bar/touch_bar.dart';

import 'aio_sign_in.dart';

final Map<String, Widget Function(BuildContext)> defaultRoutes = {
  '/': (context) => const HomeRoute(),
  '/settings': (context) => const SettingsRoute(),
  '/signin': (context) => const AIOSignInRoute(),
};

const Map<String, String> _commonRouteNames = {
  "Sign In": "/signin",
  "Settings": "/settings",
  "Home": "/",
};

class MyRouting extends ChangeNotifier {
  MyRouting({
    required this.routes,
    this.commonRouteNames = _commonRouteNames,
    this.initialRoute = '/',
  });

  final Map<String, Widget Function(BuildContext)> routes;
  final Map<String, String> commonRouteNames;
  final String initialRoute;

  String toRoute(String name) {
    debugPrint("toRoute: $name");
    return commonRouteNames[commonRouteNames.keys.firstWhere(
        (commonName) => name.toLowerCase() == commonName.toLowerCase(),
        orElse: () => throw Exception('No route found for $name'))] as String;
  }

  void registerAsync(BuildContext context) async {
    commonRouteNames;
    if (Platform.isMacOS | Platform.isLinux | Platform.isWindows) {
      debugPrint(
          "Yay, we're on menubar supporting platform; registering menubar actions and menu items");

      final TouchBar touchBar;
      List<TouchBarItem> touchBarItems = [];

      final NativeSubmenu menu;
      final List<NativeMenuItem> menuItems = [];

      commonRouteNames.forEach((name, route) {
        debugPrint("  Rigging $name -> $route");
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

      if (Platform.isMacOS) {
        debugPrint("Registering touch bar for macOS ...");
        setTouchBar(touchBar);
      }
      setApplicationMenu([menu]);
    }
  }
}
