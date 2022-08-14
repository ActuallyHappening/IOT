import 'package:flutter/material.dart';

class aio_signIn_route extends StatefulWidget {
  const aio_signIn_route({super.key});

  @override
  State<aio_signIn_route> createState() => _aio_signIn_routeState();
}

class _aio_signIn_routeState extends State<aio_signIn_route> {
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
