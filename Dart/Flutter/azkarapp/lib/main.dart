// ignore_for_file: avoid_print

import 'package:azkarapp/auth/singin.dart';
import 'package:azkarapp/firebase_options.dart';
import 'package:azkarapp/homepage.dart';
import 'package:azkarapp/auth/page.dart';
import 'package:azkarapp/notehomepage.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:azkarapp/fristpage.dart';
import 'package:flutter/material.dart';
import 'package:azkarapp/secondpage.dart';
import 'package:azkarapp/forth_page.dart';
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(const MyApp());
}

void printme(int i) {
  i++;
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  void initState() {
    FirebaseAuth.instance.authStateChanges().listen((User? user) {
            if (user == null) {
        print('User is currently signed out!');
      } else {
        print('User is signed in!');
      }
    });
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute:
          FirebaseAuth.instance.currentUser != null ? "page6" : "page1",
      theme: ThemeData(
          fontFamily: "Anta",
          appBarTheme: const AppBarTheme(
            color: Colors.red,
          ),
          textTheme: const TextTheme(
            bodySmall: TextStyle(fontFamily: "Anta", fontSize: 10),
            bodyMedium: TextStyle(fontFamily: "Anta", fontSize: 12),
            bodyLarge: TextStyle(fontFamily: "Anta", fontSize: 14),
          )),
      routes: {
        "pageone": (context) => const Fristpage(),
        "page1": (context) => Page1(),
        "pagetwo": (context) => const SecondPage(),
        "page3": (context) => const MyApp(),
        "page4": (context) => const Forthpage(),
        "singin": (context) => SingIn(),
        "page5": (context) => const Homepage(),
        "page6": (context) => const NoteHomePage(),
      },
      debugShowCheckedModeBanner: false,
      // home:  homepage()
    );
  }
}
