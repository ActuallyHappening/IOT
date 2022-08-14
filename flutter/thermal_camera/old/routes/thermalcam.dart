import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

import '../old/AIO/AIO.dart' as AIO;
import '../old/AIO/AIORenderer.dart';

Future main() async {
  await dotenv.load(fileName: ".env");
  runApp(const ThermalCamRoute());
}

class ThermalCamRoute extends StatefulWidget {
  const ThermalCamRoute({super.key});

  @override
  State<ThermalCamRoute> createState() => _ThermalCamRouteState();
}

class _ThermalCamRouteState extends State<ThermalCamRoute> {
  late Future<AIO.ThermalStream> currentStream;

  @override
  void initState() {
    super.initState();
    currentStream = AIO.fetchStream();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Fetch Data Example',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: Scaffold(
          appBar: AppBar(
            title: const Text('Fetch Data Example'),
          ),
          body: Row(children: [
            ElevatedButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: const Text("Back to index")),
            Center(
              child: FutureBuilder<AIO.ThermalStream>(
                future: currentStream,
                builder: (context, snapshot) {
                  if (snapshot.hasData) {
                    return createFromParsedStream(
                        stream: snapshot.data!.parse());
                  } else if (snapshot.hasError) {
                    return Text('${snapshot.error}');
                  }

                  // By default, show a loading spinner.
                  return const CircularProgressIndicator();
                },
              ),
            ),
          ]),
        ));
  }
}
