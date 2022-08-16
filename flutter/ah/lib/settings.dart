import 'package:flutter/material.dart';
import 'package:touch_bar/touch_bar.dart';

class settings_route extends StatefulWidget {
  const settings_route({Key? key}) : super(key: key);

  @override
  State<settings_route> createState() => _settings_routeState();
}

class _settings_routeState extends State<settings_route> {
  Future<void> asyncStuffHere() async {
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

  @override
  void initState() {
    super.initState();
    asyncStuffHere();
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
