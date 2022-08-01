import 'package:flutter/material.dart';

Widget createFromParsedStream({required List<List<int>> stream}) {
  return ListView(
    children: stream.map((row) {
      return Row(
        children: row.map((pixel) {
          return Container(
            color: Color(pixel),
            width: 10,
            height: 10,
          );
        }).toList(),
      );
    }).toList(),
  );
}
