import 'package:ah/aio_sign_in.dart';
import 'package:ah/settings.dart';
import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  static final Map<String, String> _routeNames = {
    "Sign In": "/signin",
    "Settings": "/settings",
    "Home": "/",
  };

  static final Map<String, Widget Function(BuildContext)> _routes = {
    '/': (context) => const aio_signIn_route(),
    '/settings': (context) => const settings_route(),
    '/signin': (context) => const aio_signIn_route(),
  };

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: "/",
      routes: _routes,
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  ListTile _generateDrawerOption(
      {required String title, required IconData icon}) {
    final routeName = MyApp._routeNames[title];
    if (routeName == null) {
      throw Exception("No route name for $title");
    }
    return ListTile(
      leading: Icon(icon),
      title: Text(title),
      subtitle: Text("Go to $title"),
      onTap: () {
        print("Going to $routeName");
        Navigator.pushNamed(context, routeName);
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
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
        child: ListWheelScrollView(
          itemExtent: 30,
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
