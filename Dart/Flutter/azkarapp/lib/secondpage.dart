// ignore_for_file: unused_import, camel_case_types
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:convert';
import 'package:azkarapp/homepage.dart';
import 'package:flutter/material.dart';
import 'package:azkarapp/secondpage.dart';
import 'package:azkarapp/forth_page.dart';
import 'package:http/http.dart';

class Second_Page extends StatefulWidget {
  const Second_Page({super.key});

  @override
  State<Second_Page> createState() => _Second_PageState();
}

class _Second_PageState extends State<Second_Page> {
  bool loading = false;
  List date = [];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Azkar App"),
      ),
      body: ListView(
        children: [
          MaterialButton(
            onPressed: () => showDialog(builder: (context) =>const AlertDialog(
              title: Text("Go To"),
              content: Text("Go To Second Page"),
              
            ),context: context),
            child: const Text("dsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsds . "),
          ),
          if (loading)
            const Center(
                child: CircularProgressIndicator(
              color: Colors.blue,
            )),
          ...List.generate(
            date.length,
            (index) => Card(
              child: ListTile(
                title: Text(
                  date[index]["title"],
                ),
                subtitle: Text(date[index]["body"]),
              ),
            ),
          ),
          Builder(builder: (context) {
            return MaterialButton(
              child: const Text("Go To Page 4"),
              onPressed: () {
                Navigator.of(context).pushNamed("page4");
              },
            );
          })
        ],
      ),
    );
  }
}
