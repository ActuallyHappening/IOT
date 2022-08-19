// Implements the touch and menu bars for easy use.

import 'dart:io';

import 'package:flutter/material.dart';
import 'package:menubar/menubar.dart';
import 'package:touch_bar/touch_bar.dart';
import 'package:touch_bar_platform_interface/models/touch_bar_item.dart'
    show AbstractTouchBarItem;

import 'routing.dart';

class HighLevelAction {
  HighLevelAction({required this.tb, required this.menu});

  factory HighLevelAction.make() {
    return HighLevelAction(
        tb: TouchBarButton(),
        menu: NativeSubmenu(label: 'Home', children: [
          NativeMenuItem(
              label: 'Home',
              onSelected: () {
                //
              })
        ]));
  }

  factory HighLevelAction.clickAction(
      {required String label, VoidCallback? onSelected}) {
    return HighLevelAction(
        tb: TouchBarButton(label: label, onClick: onSelected),
        menu: NativeMenuItem(label: label, onSelected: onSelected));
  }

  /// Can contain a [TouchBarPopover] which has a [TouchBarScrubber]
  final AbstractTouchBarItem tb;

  /// Is a single button in the menu bar
  final AbstractNativeMenuItem menu;
}

/// Implements the touch and menu bars for easy use using [HighLevelAction]s.
/// If none provided, the default [HighLevelAction]s are used from [MyRouting].
/// provide [useDefault] if the default HighLevelActions are still wanted from [MyRouting].
void initHighLevel(BuildContext context,
    {List<HighLevelAction>? actions = const [], bool useDefault = true}) async {
  final TouchBar tb;
  final List<NativeSubmenu> menu;

  // ignore: no_leading_underscores_for_local_identifiers
  List<HighLevelAction> _actions; // actions after defaults are loaded if needed
  _actions = [];
  _actions.addAll([
    HighLevelAction(
        tb: TouchBarButton(),
        menu: NativeSubmenu(label: 'Home', children: [
          NativeMenuItem(
              label: 'Home',
              onSelected: () {
                //
              })
        ]))
  ]);
  if (actions == null) {
    /// Set [useDefault] to true and instantiate [_actions] with empty list
    _actions = [];
  } else {
    _actions = actions;
  }
  if (useDefault) {
    // Load defaults from MyRouting
    final defaults = await MyRouting().getHighLevelActions(context);
    _actions = _actions.toList();
    _actions.addAll(defaults);
  }

  if (Platform.isMacOS) {
    debugPrint("Registering touch bar for macOS ...");
    tb = TouchBar(
      children: _actions.map((action) => action.tb).toList(),
    );
    setTouchBar(tb);
  }
  if (Platform.isLinux || Platform.isWindows || Platform.isMacOS) {
    debugPrint("Registering menu for Linux/Windows/macOS ...");
    final abstractMenu = _actions.map((action) => action.menu).toList();
    // TODO add abstract menu items to menu bar by grouping them in submenus
    List<NativeMenuItem> looseMenuItems = [];
    for (final abstractItem in abstractMenu) {
      if (abstractItem is NativeSubmenu) {
        // return abstractItem;
      } else if (abstractItem is NativeMenuItem) {
        looseMenuItems.add(abstractItem);
        // return null;
      } else {
        debugPrint("ERR: Unknown menu item type: ${abstractItem.runtimeType}");
        throw Exception("Unknown menu item type: ${abstractItem.runtimeType}");
      }
    }).toList();
    menu = looseMenuItems.cast(); // Might error, be careful!
    setApplicationMenu(menu);
  }
}
