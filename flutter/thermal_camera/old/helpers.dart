int mapNumRange(
    {required int value,
    required int min,
    required int max,
    required int newMin,
    required int newMax}) {
  return (value - min) * (newMax - newMin) ~/ (max - min) + newMin;
}
