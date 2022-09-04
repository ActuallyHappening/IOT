import 'package:ah_portal/views/views.dart';
import 'package:flutter/material.dart';

class DebugView extends StatelessWidget implements Viewable {
  const DebugView({super.key, this.drawer});

  @override
  final Widget? drawer;

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Debug Page',
      home: DebugInfoWidget(),
    );
  }
}

class DebugInfoWidget extends StatelessWidget {
  const DebugInfoWidget({super.key, this.drawer});

  final Widget? drawer;

  static const String _headerImage =
      "https://en.gravatar.com/userimage/223688227/4db4c41ba91ea03e7c43a76023782588.png";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: drawer,
      appBar: AppBar(
        title: const Text('Debug Page'),
      ),
      body: CustomScrollView(
        slivers: <Widget>[
          // SliverAppBar(
          //   title: const Text('Debug Info'),
          //   pinned: true,
          //   stretch: true,
          //   onStretchTrigger: () async {
          //     // Function callback for stretch
          //     debugPrint("onStretchTrigger");
          //     return;
          //   },
          //   expandedHeight: 200.0,
          //   flexibleSpace: FlexibleSpaceBar(
          //     stretchModes: const [
          //       StretchMode.zoomBackground,
          //       StretchMode.fadeTitle,
          //       StretchMode.blurBackground,
          //     ],
          //     title: const Text('Debug Info'),
          //     background: DecoratedBox(
          //       position: DecorationPosition.foreground,
          //       decoration: BoxDecoration(
          //         gradient: LinearGradient(
          //           begin: Alignment.bottomCenter,
          //           end: Alignment.center,
          //           colors: <Color>[Colors.teal[800]!, Colors.transparent],
          //         ),
          //       ),
          //       child: Image.network(
          //         _headerImage,
          //         fit: BoxFit.cover,
          //       ),
          //     ),
          //   ),
          // ),
          SliverList(
            delegate: SliverChildBuilderDelegate(
              (BuildContext context, int index) {
                return Container(
                  alignment: Alignment.center,
                  color: Colors.lightBlue[100 * (index % 9)],
                  height: 100.0,
                  child: Text('list item $index'),
                );
              },
              childCount: 5,
            ),
          ),
        ],
      ),
    );
  }
}
