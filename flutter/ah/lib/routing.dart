import 'package:ah/settings.dart';
import 'package:flutter/material.dart';

import 'aio_sign_in.dart';

class MyRouting {
  static final Map<String, Widget Function(BuildContext)> routes = {
    '/': (context) => const aio_signIn_route(),
    '/settings': (context) => const settings_route(),
    '/signin': (context) => const aio_signIn_route(),
  };

  static String toRoute(String name) {
    return commonRouteNames.keys.firstWhere(
        (commonName) => name.toLowerCase() == commonName.toLowerCase(),
        orElse: () => throw Exception('No route found for $name'));
  }

  static final Map<String, String> commonRouteNames = {
    "Sign In": "/signin",
    "Settings": "/settings",
    "Home": "/",
  };
}
