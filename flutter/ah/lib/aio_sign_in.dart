import 'package:flutter/material.dart';

class aio_signin_route extends StatefulWidget {
  const aio_signin_route({super.key});

  @override
  State<aio_signin_route> createState() => _aio_signin_routeState();
}

class _aio_signin_routeState extends State<aio_signin_route> {
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
