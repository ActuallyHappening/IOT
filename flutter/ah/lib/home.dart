import 'package:ah/high_level_actions.dart';
import 'package:ah/routing.dart';
import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';

const String title = "Actually Happening Portal Home";

class HomeRoute extends StatefulWidget {
  const HomeRoute({super.key});

  @override
  State<HomeRoute> createState() => _HomeRouteState();
}

class _HomeRouteState extends State<HomeRoute> {
  int _counter = 0;
  final MyRouting _routing = MyRouting();

  @override
  void initState() {
    super.initState();
    // _routing.registerAsync(context);
    initHighLevel(context,
        actions: [
          HighLevelAction.clickAction(
              label: 'Increment',
              onSelected: () {
                setState(() {
                  _counter++;
                });
              }),
        ],
        useDefault: true);
    return;
  }

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  ListTile _generateDrawerOption(
      {required String title, required IconData icon}) {
    return ListTile(
      leading: Icon(icon),
      title: Text(title),
      subtitle: Text("Go to $title"),
      onTap: () {
        _routing.to(context, name: title);
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            AnimatedTextKit(
              animatedTexts: [
                TyperAnimatedText(
                  'You have pushed the button this many times:',
                  // speed: const Duration(milliseconds: 50),
                )
              ],
              repeatForever: true,
              pause: const Duration(milliseconds: 1000),
              displayFullTextOnTap: true,
              stopPauseOnTap: true,
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        heroTag: "increment",
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
      drawer: Drawer(
        child: ListView(
          children: [
            _generateDrawerOption(title: 'Home', icon: Icons.home),
            _generateDrawerOption(title: 'Sign In', icon: Icons.account_circle),
            _generateDrawerOption(title: 'Settings', icon: Icons.settings),
          ],
        ),
      ),
    );
  }
}
