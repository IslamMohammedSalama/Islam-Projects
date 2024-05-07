// ignore_for_file: avoid_print, unused_import
import 'package:azkarapp/auth/singin.dart';
import 'package:azkarapp/firebase_options.dart';
import 'package:azkarapp/homepage.dart';
import 'package:azkarapp/auth/page.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:azkarapp/fristpage.dart';
import 'package:azkarapp/package/bs.dart';
import 'package:drop_down_list/model/selected_list_item.dart';
import 'package:flutter/material.dart';
import 'package:azkarapp/secondpage.dart';
import 'package:azkarapp/forth_page.dart';
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(const  MyApp());
}

void printme(int i) {
  i++;

  print("print me plase $i");
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
    });    super.initState();
  }
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: FirebaseAuth.instance.currentUser != null ? "page5" : "page1",
      theme: ThemeData(
        
          fontFamily: "Anta",
          appBarTheme:  const AppBarTheme(
            color: Colors.red,
          ),
          textTheme:  const TextTheme(
            bodySmall: TextStyle(fontFamily: "Anta", fontSize: 10),
            bodyMedium: TextStyle(fontFamily: "Anta", fontSize: 12),
            bodyLarge: TextStyle(fontFamily: "Anta", fontSize: 14),
          )
          
          ),
      routes: {
        "pageone": (context) =>  const fristpage(),
        "page1": (context) =>  Page1(),
        "pagetwo": (context) =>  const Second_Page(),
        "page3": (context) => const MyApp(),
        "page4": (context) =>  const forth_page(),
        "singin": (context) =>   SingIn(),
        "page5": (context) =>  const homepage(),
      },
      debugShowCheckedModeBanner: false,
      // home:  homepage()
    );
  }
}
