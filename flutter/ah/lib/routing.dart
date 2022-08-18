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
    return commonRouteNames[commonRouteNames.keys.firstWhere(
        (commonName) => name.toLowerCase() == commonName.toLowerCase(),
        orElse: () => throw Exception('No route found for $name'))] as String;
  }

  /// Navigates to the specified route by either [name] or [route].
  void to(BuildContext context, {String? name, String? route}) {
    assert(name != null || route != null);
    assert(!(name == null && route == null));
    final String routeName;
    if (name != null) {
      routeName = toRoute(name);
    } else if (route != null) {
      routeName = route;
    } else {
      throw Exception('No usable option found for name $name and route $route');
    }
    debugPrint("to: $routeName");
    Navigator.restorablePushNamed(context, routeName);
  }

  void registerAsync(BuildContext context) async {
    commonRouteNames;
    if (Platform.isMacOS | Platform.isLinux | Platform.isWindows) {
      debugPrint(
          "Yay, we're on menubar supporting platform; registering menubar actions and menu items");

      final TouchBar tb;
      List<TouchBarScrubberItem> tbRouteButtons = [];
      TouchBarScrubber tbRouteScrubber;

      final NativeSubmenu menu;
      final List<NativeMenuItem> mRouteButtons = [];

      commonRouteNames.forEach((name, route) {
        debugPrint("  Rigging $name -> $route");
        tbRouteButtons.add(TouchBarScrubberLabel(
          name,
        ));
        mRouteButtons.add(NativeMenuItem(
          label: name,
          onSelected: () {
            to(context, name);
          },
        ));
      });

      tbRouteScrubber = TouchBarScrubber(
        children: tbRouteButtons,
        mode: ScrubberMode.fixed,
        selectedStyle: ScrubberSelectionStyle.roundedBackground,
        overlayStyle: ScrubberSelectionStyle.outlineOverlay,
        onSelect: (itemIndex) {
          debugPrint("  Scrubber selected $itemIndex");
          to(context, toRoute(commonRouteNames.keys.elementAt(itemIndex)));
        },
        onHighlight: (itemIndex) {
          debugPrint(
              "Highlighted ${commonRouteNames.keys.elementAt(itemIndex)}");
        },
      );

      tb = TouchBar(children: [
        TouchBarPopover(
          label: 'Routes',
          children: [tbRouteScrubber],
          showCloseButton: true,
        )
      ]);
      menu = NativeSubmenu(label: "Screens", children: mRouteButtons);

      if (Platform.isMacOS) {
        debugPrint("Registering touch bar for macOS ...");
        setTouchBar(tb);
      }
      setApplicationMenu([menu]);
    }
  }
}
