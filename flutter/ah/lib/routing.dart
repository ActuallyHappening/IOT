import 'package:ah/high_level_actions.dart';
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
  /// Singleton design pattern, use like `MyRouting()` to obtain
  /// Contains the necessary information for the routing
  factory MyRouting() => _instance;

  /// Used to construct dynamically
  /// Don't construct this directly, use [MyRouting] Singleton instead
  /// Like: `MyRouting()`
  MyRouting.from({
    required this.routes,
    this.commonRouteNames = _commonRouteNames,
    this.initialRoute = Navigator.defaultRouteName, // '/',
  });
  static final MyRouting _instance = MyRouting._singleton(
      routes: defaultRoutes,
      commonRouteNames: _commonRouteNames,
      initialRoute: Navigator.defaultRouteName);

  MyRouting._singleton({
    required this.routes,
    this.commonRouteNames = _commonRouteNames,
    this.initialRoute = Navigator.defaultRouteName, // '/',
  });

  final Map<String, Widget Function(BuildContext)> routes;
  final Map<String, String> commonRouteNames;
  final String initialRoute;

  /// Takes a [name] like 'Home' and maps it to '/'
  String toRoute(String name) {
    return commonRouteNames[commonRouteNames.keys.firstWhere(
        (commonName) => name.toLowerCase() == commonName.toLowerCase(),
        orElse: () => throw Exception('No route found for $name'))] as String;
  }

  /// Navigates to the specified route by either [name] or [route].
  /// If given a [name], it will be converted to a [route] using [toRoute].
  /// If given a [route], it will be navigated to using internal methods of [Navigator]
  /// whose exact implementations are not guaranteed.
  ///
  /// If navigating to the 'home' route, attempts to restore its state for the Touch and Menu Bars.
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
    if (routeName == initialRoute) {
      // If route requested is home route
      debugPrint("() Home detected");
      if (!Navigator.canPop(context)) {
        // Already on home page (or other root route)
        debugPrint("() On Home page?");
        return;
      }
      debugPrint("() Popping until home page, can pop");
      // Navigator.popUntil(context, ModalRoute.withName(initialRoute));
      // Removes old routing widgets from history
      Navigator.pushNamedAndRemoveUntil(
          context, routeName, (Route<dynamic> route) => false);
      return;
    }
    Navigator.restorablePushNamed(context, routeName);
  }

  Future<List<HighLevelAction>> getHighLevelActions(
      BuildContext context) async {
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
          to(context, name: name);
        },
      ));
    });

    String routeFromNum(int num) {
      return commonRouteNames.keys.elementAt(num);
    }

    tbRouteScrubber = TouchBarScrubber(
      children: tbRouteButtons,
      mode: ScrubberMode.fixed,
      selectedStyle: ScrubberSelectionStyle.roundedBackground,
      overlayStyle: ScrubberSelectionStyle.outlineOverlay,
      onSelect: (itemIndex) {
        debugPrint("> Scrubber selected ${routeFromNum(itemIndex)}");
        to(context, name: toRoute(routeFromNum(itemIndex)));
      },
      onHighlight: (itemIndex) {
        debugPrint("> Highlighted ${routeFromNum(itemIndex)}");
        to(context, name: toRoute(routeFromNum(itemIndex)));
      },
    );

    final tb = TouchBarPopover(
      label: 'Routes',
      children: [tbRouteScrubber],
      showCloseButton: true,
    ); // Don't know if this will work at runtime ???
    menu = NativeSubmenu(label: "Screens", children: mRouteButtons);
    return [
      HighLevelAction(
        tb: tb,
        menu: menu,
      ),
    ];
  }
}
