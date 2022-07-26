import 'dart:convert';

import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:http/http.dart' as http;

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

  static const defaultDimensions = [
    32,
    24,
  ];

  const ThermalStream({required this.stream});

  static Future<ThermalStream> fetch() async {
    return await fetchStream();
  }

  static List<List<int>> _parse({required List<int> stream}) {
    const dimensions = defaultDimensions;
    final width = dimensions[0];
    final height = dimensions[1];
    final pixels = List<List<int>>.generate(height, (y) {
      return List<int>.generate(width, (x) {
        final index = y * width + x;
        return stream[index];
      });
    });
    return pixels;
  }

  List<List<int>> parse() {
    /* Construct ThermalStream from Json and call ThermalStream.parse() on it */
    return _parse(stream: stream);
  }

  factory ThermalStream.fromJson(Map<String, dynamic> json) {
    final value = jsonDecode(json['value']);
    final rawStream = value['stream'];
    final List<dynamic> parsedStream;
    try {
      parsedStream = rawStream as List<dynamic>;
    } on FormatException {
      throw Exception(
          'Invalid stream data (probably cam not plugged in), got $rawStream');
    } catch (e) {
      throw Exception('Invalid stream data (probably corrupted data), e=$e');
    }
    // parsedStream = "[$rawStream]";
    final List<int> finishedStream;
    try {
      finishedStream = parsedStream.map((e) => e as int).toList();
    } catch (e) {
      throw Exception(
          'Invalid stream data (probably corrupted or NaN data)\n Raw error = $e');
    }
    return ThermalStream(stream: finishedStream);
  }
}
