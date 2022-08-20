import 'package:ah/high_level_actions.dart';
import 'package:flutter/material.dart';

class SettingsRoute extends StatefulWidget {
  const SettingsRoute({Key? key}) : super(key: key);

  @override
  State<SettingsRoute> createState() => _SettingsRouteState();
}

class _SettingsRouteState extends State<SettingsRoute> {

  @override
  void initState() {
    super.initState();
    initHighLevel(context, actions: [
      HighLevelAction.clickAction(
          label: 'Change Setting',
          onSelected: () {
            debugPrint('Change Setting');
          }),
    ]);
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
