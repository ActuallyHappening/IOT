import 'package:ah_portal/views/views.dart';
import 'package:flutter/material.dart';

class DefaultHomeView extends StatelessWidget implements Viewable {
  const DefaultHomeView({super.key, this.drawer});

  @override
  final Widget? drawer;

  @override
  Widget build(BuildContext context) {
    return DefaultHomeWidget(drawer: drawer);
  }
}

class DefaultHomeWidget extends StatelessWidget {
  const DefaultHomeWidget({super.key, this.drawer});

  final Widget? drawer;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: const Center(
        child: Text('Default Home Page'),
      ),
      drawer: drawer,
    );
  }
}
