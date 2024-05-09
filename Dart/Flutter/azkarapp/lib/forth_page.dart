
import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'dart:convert';

class Forthpage extends StatefulWidget {
  const Forthpage({super.key});

  @override
  State<Forthpage> createState() => _ForthpageState();
}

class _ForthpageState extends State<Forthpage> {
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
