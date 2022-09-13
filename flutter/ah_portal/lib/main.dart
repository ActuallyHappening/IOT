import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import 'package:ah_portal/views/default.dart';

import 'firebase_options.dart';

Future<void> main() async {
  // Wait for binding
  WidgetsFlutterBinding.ensureInitialized();
  // allow/stop google fonts from http requests
  GoogleFonts.config.allowRuntimeFetching = true;
  // Firebase init app
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  // FirebaseDatabase.instance.setPersistenceEnabled(true);
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  WidgetBuilder _makeView(Widget widget) {
    return (BuildContext context) => Scaffold(
          // drawer: _drawer(context),
          // drawer: Image.asset('assets/images/teeth_only_brand.jpg'),
          appBar: AppBar(
              // title: const Text('Thermal Camera Live Feed'),
              backgroundColor: const Color.fromARGB(255, 92, 192, 230),
              title: SizedBox(
                height: 40.0, // height of the button
                width: MediaQuery.of(context).size.width * 0.8,
                child: Container(
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(10.0),
                    ),
                    child: Image.asset('assets/images/horizontal_brand.png')),
              )),
          // backgroundColor: Color.fromARGB(255, 92, 192, 230),
          backgroundColor: Color.fromARGB(255, 58, 127, 169),
          body: widget,
        );
  }

  Widget _drawer(BuildContext context) => Drawer(
        child: ListView(
          children: [
            const DrawerHeader(
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
              margin: EdgeInsets.only(bottom: 16),
              padding: EdgeInsets.all(64),
              child: Text(
                'Other options below ...',
                // textScaleFactor: 1.5,
              ),
            ),
            ListTile(
              title: const Text('Go to Home'),
              leading: const Icon(Icons.home),
              onTap: () {
                Navigator.of(context).pushNamed('/');
              },
            ),
            ListTile(
              title: const Text('Go to Settings'),
              leading: const Icon(Icons.settings),
              onTap: () {
                Navigator.of(context).pushNamed('/');
              },
            ),
          ],
        ),
      );

  ThemeData _buildTheme(brightness) {
    ThemeData baseTheme =
        ThemeData(primarySwatch: Colors.blue, brightness: brightness);
    return baseTheme.copyWith(
        textTheme: GoogleFonts.robotoSerifTextTheme(baseTheme.textTheme));
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Smile Pal Live Camera Feed',
      theme: _buildTheme(Brightness.dark),
      initialRoute: "/",
      routes: <String, WidgetBuilder>{
        '/': _makeView(DefaultHomeWidget()),
        // '/image': _makeView(const ImageTester()),
      },
    );
  }
}
