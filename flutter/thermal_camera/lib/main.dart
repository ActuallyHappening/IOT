import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  static const _title = "Flutter layout tutorial";

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: _title,
      home: Scaffold(
        appBar: AppBar(
          title: const Text(_title),
        ),
        body: Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          const Center(
          child: Text('Hello World'),
          ),
          const Center(child: Text("Yay!")),
          CachedNetworkImage(
<<<<<<< HEAD
            imageUrl: "http://via.placeholder.com/350",
=======
            imageUrl: "http://via.placeholder.com/350x150",
>>>>>>> ef5bf8b3f2060c35639e9d4cc5810ec59203b1b2
            progressIndicatorBuilder: (context, url, downloadProgress) =>
                CircularProgressIndicator(value: downloadProgress.progress),
            errorWidget: (context, url, error) => const Icon(Icons.error),
          ),
          Icon(Icons.alarm, color: Colors.red[600])
        ]),
      ),
    );
  }
}
