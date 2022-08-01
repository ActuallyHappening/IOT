// ignore_for_file: file_names

import 'package:flutter/material.dart';

import '../helpers.dart';

const double scale = 30;
const int _lowestTemp = 0;
const int _highestTemp = 70;

Widget createFromParsedStream({required List<List<int>> stream}) {
  return ListView(
    children: stream.map((row) {
      return Row(
        children: row.map((pixel) {
          return Container(
            color: const Color(0xFF000000).withRed(mapNumRange(
                value: pixel,
                min: _lowestTemp,
                max: _highestTemp,
                newMin: 0,
                newMax: 255)),
            // color: Color(pixel),
            width: scale,
            height: scale,
          );
        }).toList(),
      );
    }).toList(),
  );
}
