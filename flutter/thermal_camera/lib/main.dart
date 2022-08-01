import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import 'package:flutter_dotenv/flutter_dotenv.dart';

Future<ThermalStream> fetchStream() async {
  final String username = dotenv.env["ADAFRUIT_IO_USERNAME"] as String;
  final String key = dotenv.env["ADAFRUIT_IO_KEY"] as String;
  final response = await http.get(
      Uri.parse(
          'https://io.adafruit.com/api/v2/$username/feeds/brad.ir-stream/data?limit=1'),
      headers: {'X-AIO-KEY': key});

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    final streamData = json.decode(response.body)[0];
    return ThermalStream.fromJson(streamData);
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load album');
  }
}

class ThermalStream {
  final List<int> stream;

  const ThermalStream({required this.stream});

  static Future<ThermalStream> fetch() async {
    return await fetchStream();
  }

  factory ThermalStream.fromJson(Map<String, dynamic> json) {
    final value = jsonDecode(json['value']);
    return ThermalStream(
      stream: value['stream'],
    );
  }
}

Future main() async {
  await dotenv.load(fileName: ".env");
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  late Future<ThermalStream> currentStream;

  @override
  void initState() {
    super.initState();
    currentStream = fetchStream();
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
        body: Center(
          child: FutureBuilder<ThermalStream>(
            future: currentStream,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                return Text(snapshot.data!.stream.toString());
              } else if (snapshot.hasError) {
                return Text('${snapshot.error}');
              }

              // By default, show a loading spinner.
              return const CircularProgressIndicator();
            },
          ),
        ),
      ),
    );
  }
}
