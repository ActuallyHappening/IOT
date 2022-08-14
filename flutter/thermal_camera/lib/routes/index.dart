import 'package:flutter/material.dart';
import 'package:thermal_camera/routes/thermalcam.dart';

class IndexRoute extends StatelessWidget {
  const IndexRoute({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Index Route'),
      ),
      body: Center(
        child: ElevatedButton(
          child: const Text('Open Thermal Camera Page :)'),
          onPressed: () {
            // Navigator.pushNamed(context, '/second');
            Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) => const ThermalCamRoute()));
          },
        ),
      ),
    );
  }
}
