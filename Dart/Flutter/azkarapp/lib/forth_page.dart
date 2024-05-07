// ignore_for_file: unused_import, camel_case_types
import 'package:azkarapp/homepage.dart';
import 'package:drop_down_list/model/selected_list_item.dart';
import 'package:flutter/material.dart';
import 'package:azkarapp/secondpage.dart';
import 'package:azkarapp/forth_page.dart';
import 'package:http/http.dart';
import 'dart:convert';
import 'package:azkarapp/package/bs.dart';
import 'package:shared_preferences/shared_preferences.dart';

class forth_page extends StatefulWidget {
  const forth_page({super.key});

  @override
  State<forth_page> createState() => _forth_pageState();
}

class _forth_pageState extends State<forth_page> {
  bool loadingg = true;
  Future<List> getdate() async {
    var respo =
        await get(Uri.parse("http://jsonplaceholder.typicode.com/posts"));
    List respobpday = jsonDecode(respo.body);
    loadingg = false;
    return respobpday;
  }

  // @override
  // void initState() {
  //   getdate();
  //   super.initState();
  // }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: FutureBuilder<List>(
          future: getdate(),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return const Center(
                child: CircularProgressIndicator(),
              );
            }

            if (snapshot.connectionState == ConnectionState.done) {
              if (snapshot.hasError) {
                return Center(
                    child: Text(
                  "Error : ${snapshot.error}",
                  style: const TextStyle(fontSize: 20),
                ));
              }
              return ListView.builder(
                itemCount: snapshot.data!.length,
                itemBuilder: (context, index) => Card(
                  child: ListTile(
                    title: Text(
                      "${snapshot.data![index]["title"]}",
                      style: const TextStyle(fontFamily: "Anta"),
                    ),
                    subtitle: Text(
                      "${snapshot.data![index]["body"]}",
                      style: const TextStyle(fontFamily: "Anta"),
                    ),
                  ),
                ),
              );
            }

            return const Text("");
          }),
      appBar: AppBar(
        title: const Text(
          "Azkar App 2",
        ),
        centerTitle: true,
      ),
    );
  }
}
