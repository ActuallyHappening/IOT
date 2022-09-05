// File generated by FlutterFire CLI.
// ignore_for_file: lines_longer_than_80_chars, avoid_classes_with_only_static_members
import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, kIsWeb, TargetPlatform;

/// Default [FirebaseOptions] for use with your Firebase apps.
///
/// Example:
/// ```dart
/// import 'firebase_options.dart';
/// // ...
/// await Firebase.initializeApp(
///   options: DefaultFirebaseOptions.currentPlatform,
/// );
/// ```
class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        return macos;
      case TargetPlatform.windows:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for windows - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      case TargetPlatform.linux:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for linux - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      default:
        throw UnsupportedError(
          'DefaultFirebaseOptions are not supported for this platform.',
        );
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyA63ZORAodp0lMe7vplwWSRgk9mbZ_Rt5c',
    appId: '1:431633313063:web:815ae5d0e6942470110d02',
    messagingSenderId: '431633313063',
    projectId: 'actually-happening-portal',
    authDomain: 'actually-happening-portal.firebaseapp.com',
    databaseURL: 'https://actually-happening-portal-default-rtdb.asia-southeast1.firebasedatabase.app',
    storageBucket: 'actually-happening-portal.appspot.com',
    measurementId: 'G-7P71DTW8BF',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyBVOuao7oUgPlpxh--uCyaXjA4zgYy8N0w',
    appId: '1:431633313063:android:9608feb2f188322e110d02',
    messagingSenderId: '431633313063',
    projectId: 'actually-happening-portal',
    databaseURL: 'https://actually-happening-portal-default-rtdb.asia-southeast1.firebasedatabase.app',
    storageBucket: 'actually-happening-portal.appspot.com',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyCcC7PJAkSGOSl9_chIMFoW6HeFef9Dmag',
    appId: '1:431633313063:ios:bfcee2cb778dc4af110d02',
    messagingSenderId: '431633313063',
    projectId: 'actually-happening-portal',
    databaseURL: 'https://actually-happening-portal-default-rtdb.asia-southeast1.firebasedatabase.app',
    storageBucket: 'actually-happening-portal.appspot.com',
    iosClientId: '431633313063-qbhkboo1e7mqlus3uoacfkso1evrceq0.apps.googleusercontent.com',
    iosBundleId: 'com.ah-portal.initial',
  );

  static const FirebaseOptions macos = FirebaseOptions(
    apiKey: 'AIzaSyCcC7PJAkSGOSl9_chIMFoW6HeFef9Dmag',
    appId: '1:431633313063:ios:a27f99dd59a274a6110d02',
    messagingSenderId: '431633313063',
    projectId: 'actually-happening-portal',
    databaseURL: 'https://actually-happening-portal-default-rtdb.asia-southeast1.firebasedatabase.app',
    storageBucket: 'actually-happening-portal.appspot.com',
    iosClientId: '431633313063-3flkrhsmg70uslifvfrista992rata42.apps.googleusercontent.com',
    iosBundleId: 'com.example.ahPortal',
  );
}