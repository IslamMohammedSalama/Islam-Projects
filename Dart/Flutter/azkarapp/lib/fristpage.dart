
import 'package:flutter/material.dart';


class Fristpage extends StatefulWidget {
  const Fristpage({super.key});

  @override
  State<Fristpage> createState() => _FristpageState();
}

class _FristpageState extends State<Fristpage> {
  int index = 0;
  List<Widget> screens = [];
  List usernames = [
    {"Name": "Islam", "Age": "12", "Jop": "Andorid Devoloper"},
    {"Name": "Hashem", "Age": "18", "Jop": "Web Devoloper"},
    {"Name": "Hazem", "Age": "12", "Jop": "IOS Devoloper"},
  ];
  @override
  void initState() {
    super.initState();
    // Initialize the 'screens' list here
    screens = [
      Column(
        children: [
          ...List.generate(usernames.length, (index) {
            return Card(
              child: ListTile(
                title: Text("${usernames[index]["Name"]}"),
                subtitle: Text(
                    "Age Is ${usernames[index]["Age"]} .\n Jop Is ${usernames[index]["Jop"]} ."),
              ),
            );
          }),
        ],
      ),
      MaterialButton(
        child: const Text(
          "Get Lost",
        ),
        onPressed: () {
          /* */
          showDialog(
            context: context,
            builder: (context) => AlertDialog(
              title: const Text("Go To"),
              content: const Text("Go To Second Page"),
              actions: [
                MaterialButton(
                  child: const Text("Page one"),
                  onPressed: () {
                    Navigator.of(context).pushNamed("pageone");
                  },
                ),
                MaterialButton(
                  child: const Text("back"),
                  onPressed: () {
                    Navigator.of(context).pushNamed("page3");
                  },
                ),
                MaterialButton(
                  child: const Text("Page Two"),
                  onPressed: () {
                    Navigator.of(context).pushNamed("pagetwo");
                  },
                )
              ],
            ),
          );
        },
      ),
      MaterialButton(
        onPressed: () => Navigator.of(context).pop(),
        child: const Text("Hello"),
      ),
    ];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        floatingActionButton: FloatingActionButton(
          onPressed: () {},
        ),
        bottomNavigationBar: BottomNavigationBar(
          currentIndex: index,
          type: BottomNavigationBarType.fixed,
          selectedItemColor: Colors.blue,
          unselectedItemColor: Colors.black,
          showUnselectedLabels: true,
          showSelectedLabels: false,
          iconSize: 30,
          selectedFontSize: 20,
          unselectedFontSize: 15,
          onTap: (value) {
            setState(() {
              index = value;
            });
          },
          backgroundColor: Colors.grey,
          elevation: 20,
          items: const [
            BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
            BottomNavigationBarItem(icon: Icon(Icons.backup), label: "back "),
            BottomNavigationBarItem(
                icon: Icon(Icons.person), label: "Your Account"),
          ],
        ),
        appBar: AppBar(
          title: const Text("Hello "),
          centerTitle: true,
        ),
        body: ListView(
          children: [screens.elementAt(index)],
        ));
  }
}
