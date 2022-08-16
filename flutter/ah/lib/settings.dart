import 'package:flutter/material.dart';
import 'package:menubar/menubar.dart';
import 'package:touch_bar/touch_bar.dart';

class SettingsRoute extends StatefulWidget {
  const SettingsRoute({Key? key}) : super(key: key);

  @override
  State<SettingsRoute> createState() => _SettingsRouteState();
}

class _SettingsRouteState extends State<SettingsRoute> {
  Future<void> touchBarAsync() async {
    final settingsIcon =
        await TouchBarImage.loadFrom(path: 'icons/settings.png');

    TouchBar bar = TouchBar(children: [
      TouchBarLabel('hello TOUCH BAR YAY!'),
      TouchBarButton(
          icon: settingsIcon,
          label: 'Settings',
          onClick: () {
            print("Settings clicked YAYAYAY!");
            Navigator.pop(context);
          })
    ]);
    setTouchBar(bar);
  }

  menuBarAsync() {
    setApplicationMenu([
      NativeSubmenu(label: 'TEST submenu', children: [
        NativeMenuItem(
            label: 'test item',
            onSelected: () {
              print('test item clicked');
            }),
        NativeMenuItem(
            label: 'test item 2',
            onSelected: () {
              print('test item 2 clicked');
            }),
      ]),
    ]);
  }

  @override
  void initState() {
    super.initState();
    touchBarAsync();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Settings'),
      ),
      body: ListView(
        children: const [
          Center(
            child: Text('Settings'),
          ),
        ],
      ),
    );
  }
}
