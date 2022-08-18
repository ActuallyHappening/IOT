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

  /// Can contain a [TouchBarPopover] which has a [TouchBarScrubber]
  final AbstractTouchBarItem tb;

  /// Is a single button in the menu bar
  final NativeSubmenu menu;
}

/// Implements the touch and menu bars for easy use using [HighLevelAction]s.
/// If none provided, the default [HighLevelAction]s are used from [MyRouting].
/// provide [useDefault] if the default HighLevelActions are still wanted from [MyRouting].
void initHighLevel(BuildContext context,
    {List<HighLevelAction>? actions = const [], bool useDefault = true}) async {
  final TouchBar tb;
  final List<NativeSubmenu> menu;
  // ignore: no_leading_underscores_for_local_identifiers
  final List<HighLevelAction> _actions = actions ?? [];
  if (actions == null) {
    /// Set [useDefault] to true and instantiate [_actions] with empty list
    useDefault = true;
  }
  if (useDefault) {
    _actions.addAll(await MyRouting().getHighLevelActions(context));
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
    menu = _actions.map((action) => action.menu).toList();
    setApplicationMenu(menu);
  }
}
