import 'package:flutter/material.dart';

class AIOSignInRoute extends StatefulWidget {
  const AIOSignInRoute({super.key});

  @override
  State<AIOSignInRoute> createState() => _AIOSignInRouteState();
}

class _AIOSignInRouteState extends State<AIOSignInRoute> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Sign In'),
      ),
      body: const Center(
        child: Text('Sign In'),
      ),
    );
  }
}
