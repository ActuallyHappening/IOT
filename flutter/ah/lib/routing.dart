import 'package:ah/home.dart';
import 'package:ah/settings.dart';
import 'package:flutter/material.dart';

import 'aio_sign_in.dart';

class MyRouting {
  static final Map<String, Widget Function(BuildContext)> routes = {
    '/': (context) => const HomeRoute(),
    '/settings': (context) => const SettingsRoute(),
    '/signin': (context) => const AIOSignInRoute(),
  };
  static const String initialRoute = '/';

  static String toRoute(String name) {
    print("toRoute: $name");
    return commonRouteNames[commonRouteNames.keys.firstWhere(
        (commonName) => name.toLowerCase() == commonName.toLowerCase(),
        orElse: () => throw Exception('No route found for $name'))] as String;
  }

  static final Map<String, String> commonRouteNames = {
    "Sign In": "/signin",
    "Settings": "/settings",
    "Home": "/",
  };
}
