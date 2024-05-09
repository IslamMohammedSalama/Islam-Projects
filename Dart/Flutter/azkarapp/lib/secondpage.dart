
import 'package:flutter/material.dart';

class SecondPage extends StatefulWidget {
  const SecondPage({super.key});

  @override
  State<SecondPage> createState() => _SecondPageState();
}

class _SecondPageState extends State<SecondPage> {
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
