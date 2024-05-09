import 'package:azkarapp/auth/page.dart';
import 'package:azkarapp/fristpage.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:azkarapp/package/bs.dart';
import 'package:drop_down_list/model/selected_list_item.dart';
import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';

void printme(int i) {
  i++;
}

class Homepage extends StatefulWidget {
  const Homepage({super.key});

  @override
  State<Homepage> createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  TextEditingController tec = TextEditingController();

  bool status = false;
  late ScrollController secro;
  int i = 0;
  GlobalKey<FormState> formalal = GlobalKey();
  String? usernamename;
  TextEditingController text = TextEditingController();
  bool check = false;
  String azkar = "Azkar App ";

  List names = ["Is", "Ha", "Mo", "Ah", "Al", "Ak", "Ab", "Sa"];
  GlobalKey<ScaffoldState> sk = GlobalKey();
  @override
  void initState() {
    super.initState();
    secro = ScrollController();
    secro.addListener(() {
      // print("sc ${secro.offset}");
    });
  }

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Scaffold(
        key: sk,
        drawer: Drawer(
          child: ListView.builder(
            itemCount: names.length,
            itemBuilder: (context, index) {
              return Card(
                // borderOnForeground: true,
                color: const Color.fromARGB(255, 0, 0, 0),
                child: ListTile(
                  title: Column(
                      // mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        SafeArea(
                          child: Container(
                            decoration: BoxDecoration(
                              borderRadius:
                                  const BorderRadius.all(Radius.circular(1000)),
                              border: Border.all(
                                  color:
                                      const Color.fromARGB(255, 255, 255, 255),
                                  width: 10.0),
                              color: index.isEven
                                  ? Colors.blue
                                  : const Color.fromARGB(255, 255, 17, 0),
                              boxShadow: const [
                                BoxShadow(
                                    color: Color.fromARGB(255, 255, 0, 0),
                                    spreadRadius: 5,
                                    blurRadius: 15.5,
                                    offset: Offset(-10, 20)),
                                BoxShadow(
                                    color: Color.fromARGB(255, 255, 187, 0),
                                    spreadRadius: 5,
                                    blurRadius: 15.5,
                                    offset: Offset(10, 20)),
                                BoxShadow(
                                    color: Color.fromRGBO(0, 255, 132, 1),
                                    spreadRadius: 5,
                                    blurRadius: 15.5,
                                    offset: Offset(-10, -20)),
                                BoxShadow(
                                    color: Color.fromARGB(255, 1, 45, 24),
                                    spreadRadius: 3,
                                    blurRadius: 15.5,
                                    offset: Offset(10, -20)),
                              ],
                            ),
                            margin: const EdgeInsets.fromLTRB(20, 40, 40, 20),
                            padding: const EdgeInsets.all(10.0),
                            width: 210,
                            height: 160,
                            child: Center(
                              child: Column(
                                children: [
                                  const Row(
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      Image(
                                        image: AssetImage(
                                            "assets/images/image-optimization.jpg"),
                                        width: 40.0,
                                        height: 40.0,
                                      ),
                                      Image(
                                        image: AssetImage(
                                            "assets/images/brave.png"),
                                        width: 40.0,
                                        height: 40.0,
                                      ),
                                      Image(
                                        image: AssetImage(
                                          "assets/images/vscode.png",
                                        ),
                                        height: 40.0,
                                        width: 40.0,
                                      ),
                                    ],
                                  ),
                                  Text(
                                    "Hello , ${names[index]} .",
                                    style: TextStyle(
                                      color: const Color(0xFF00FF00),
                                      fontSize: 12.5,
                                      fontWeight: FontWeight.w900,
                                      fontFamily:
                                          index.isEven ? "arial" : "serif",
                                      fontStyle: FontStyle.italic,
                                    ),
                                  ),
                                  Text(
                                    " My Name Is  ${names[index]}.",
                                    style: TextStyle(
                                      backgroundColor: index.isEven
                                          ? Colors.blue
                                          : const Color.fromARGB(
                                              255, 255, 17, 0),
                                      color: const Color.fromARGB(
                                          255, 166, 255, 166),
                                      fontSize: 12.5,
                                      fontWeight: FontWeight.w900,
                                      fontFamily: "arial",
                                      fontStyle: FontStyle.italic,
                                    ),
                                  )
                                ],
                              ),
                            ),
                          ),
                        ),
                      ]),
                  subtitle: MaterialButton(
                    onPressed: () {
                      printme;
                    },
                    color: Colors.red,
                    child: const Text(
                      "Hello",
                      // style:
                      // TextStyle(color: Color.fromARGB(100, 200, 100, 2000)),
                    ),
                  ),

                  // onTap: () => printme(),
                ),
              );
            },
          ),
        ),
        floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
        floatingActionButton: FloatingActionButton(
          backgroundColor: Colors.amber,
          foregroundColor: Colors.black,
          elevation: 10.0,
          splashColor: const Color.fromARGB(255, 255, 0, 0),
          highlightElevation: 10.0,
          child: const Icon(Icons.add),
          onPressed: () {
            setState(() {
              azkar = "Azkar App $i ";
              sk.currentState!.openDrawer();
              if (formalal.currentState!.validate()) {
                if (text.text.isEmpty) {
                  return;
                } else {
                  formalal.currentState!.save();
                  setState(() {
                    azkar = azkar + text.text;
                  });
                }

                // print(text.text);
              } else {
                return;
              }

              i++;
            });
          },
        ),
        backgroundColor: const Color.fromARGB(255, 0, 125, 40),
        body: TabBarView(
          children: [
            ListView(
              controller: secro,
              children: [
                MaterialButton(
                    color: Colors.red[200],
                    onPressed: () {
                      secro.animateTo(9386.0,
                          duration: const Duration(seconds: 5),
                          curve: Curves.fastOutSlowIn);
                    },
                    child: const Text(
                      "Jump To Bottom .",
                      style: TextStyle(fontSize: 20),
                    )),
                ...List.generate(
                    50,
                    (index) => Container(
                          alignment: Alignment.center,
                          height: 100,
                          color: index.isEven ? Colors.blue : Colors.red,
                          child: Text(
                            "Hello $index",
                            style: const TextStyle(fontSize: 20),
                          ),
                        )),
                MaterialButton(
                    color: Colors.blue[300],
                    onPressed: () {
                      secro.animateTo(0.0,
                          duration: const Duration(seconds: 5),
                          curve: Curves.fastOutSlowIn);
                    },
                    child: const Text(
                      "Jump To Top .",
                      style: TextStyle(fontSize: 20),
                    )),
              ],
            ),
            Form(
              key: formalal,
              child: ListView.builder(
                  itemCount: 5,
                  itemBuilder: (context, index) => Column(
                        children: [
                          Card(
                            margin:
                                const EdgeInsets.only(top: 20.0, bottom: 20.0),
                            color: const Color.fromARGB(255, 0, 255, 80),
                            child: ListTile(
                              leading: IconButton(
                                onPressed: () {
                                  index.isEven
                                      ? const Text("android")
                                      : const Text("apple");
                                },
                                icon: index.isEven
                                    ? const Icon(Icons.android)
                                    : const Icon(Icons.apple),
                              ),
                              trailing: index.isEven
                                  ? Switch(
                                      inactiveTrackColor: Colors.red,
                                      inactiveThumbColor: Colors.green,
                                      activeColor: Colors.blue,
                                      activeTrackColor: Colors.green,
                                      // inactiveThumbColor: Colors.red,
                                      value: status,
                                      onChanged: (statu) {
                                        setState(() {
                                          status = statu;
                                        });
                                      },
                                    )
                                  : Checkbox(
                                      value: check,
                                      onChanged: (value) => setState(() {
                                        check = value!;
                                      }),
                                    ),
                              onTap: () => printme(index),
                              title: Text(
                                "Azkar App $index",
                                style: const TextStyle(
                                    fontSize: 20.0,
                                    fontWeight: FontWeight.w900),
                              ),
                              subtitle: const Text(
                                "Hello World",
                                style: TextStyle(
                                    fontSize: 20.0,
                                    fontWeight: FontWeight.w700),
                              ),
                              textColor: Colors.cyan,
                            ),
                          ),
                          TextFormField(
                            decoration: InputDecoration(
                                border: const OutlineInputBorder(),
                                icon: const Icon(Icons.person),
                                focusedBorder: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(100)),
                                enabled: true,
                                filled: true,
                                fillColor: Colors.cyan,
                                labelText: "UserName : ",
                                suffixIcon: const Icon(Icons.person),
                                prefixIcon: const Icon(Icons.person),
                                suffixIconColor: Colors.blue,
                                prefixIconColor: Colors.red,
                                prefixText: "Name : ",
                                suffixStyle: const TextStyle(color: Colors.red),
                                prefixStyle:
                                    const TextStyle(color: Colors.blue),
                                suffixText: ": islam"),
                            keyboardType: TextInputType.visiblePassword,
                            style: const TextStyle(
                                fontSize: 10.0, fontWeight: FontWeight.bold),
                            controller: text,
                            onFieldSubmitted: (value) {},
                            autocorrect: true,
                            autovalidateMode: AutovalidateMode.always,
                            validator: (value) {
                              if (value!.isEmpty) {
                                return "enter a Username Please";
                              } else if (value.length < 3) {
                                return "Username should be more than 3";
                              }
                              return null;
                            },
                            onSaved: (newValue) => usernamename = newValue,
                          ),
                          Text("Hello $usernamename",
                              textAlign: TextAlign.center,
                              style: const TextStyle(
                                  backgroundColor: Color.fromARGB(0, 0, 0, 0),
                                  color: Colors.white)),
                        ],
                      )),
            ),
            ListView(
              children: [
                Center(
                    child: Column(
                  children: [
                    Builder(builder: (context) {
                      return MaterialButton(
                        onPressed: () {
                          showDialog(
                            context:
                                context, // Provide the context of your widget
                            builder: (context) {
                              return AlertDialog(
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(0.0),
                                ),
                                title: const Text('Are You Sure ?'),
                                content: const Text("You Will be Logout"),
                                actions: [
                                  MaterialButton(
                                    child: const Text("Yes"),
                                    onPressed: () {
                                      Navigator.of(context).pop();
                                    },
                                  )
                                ],
                              );
                            },
                          );
                        },
                        child: const Text("Hello"),
                      );
                    }),
                    Builder(builder: (context) {
                      return MaterialButton(
                        child: const Text("Home"),
                        onPressed: () {
                          Navigator.of(context).push(
                            MaterialPageRoute(
                                builder: (context) => const Fristpage()),
                          );
                        },
                      );
                    }),
                    MaterialButton(
                      onPressed: () {
                        sk.currentState!.showBottomSheet((context) => Container(
                              color: Colors.red,
                              width: 200,
                              height: 500,
                              child: MaterialButton(
                                // minWidth: 10,height: 20,
                                child: const Text("hello"),
                                onPressed: () {
                                  Navigator.of(context).pop();
                                },
                              ),
                            ));
                      },
                      child: const Text("nala"),
                    ),
                    Builder(builder: (context) {
                      return MaterialButton(
                        // minWidth: 10,height: 20,
                        child: const Text("welcome"),
                        onPressed: () {
                          ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(
                              content: Text("Hello"),
                              duration: Duration(seconds: 1),
                            ),
                          );
                        },
                      );
                    }),
                    AppTextField(
                        textEditingController: tec,
                        datelist: [
                          SelectedListItem(name: "islam"),
                          SelectedListItem(name: "hashem"),
                          SelectedListItem(name: "mohamed"),
                          SelectedListItem(name: "hazem"),
                        ],
                        title: "islam",
                        hint: "hazem",
                        isCitySelected: true),
                  ],
                )),
              ],
            )
          ],
        ),
        appBar: AppBar(
          elevation: 200.0,
          shadowColor: const Color.fromARGB(255, 255, 0, 0),
          title: Text("$azkar $i"),
          titleTextStyle: const TextStyle(fontSize: 10, color: Colors.white),
          backgroundColor: Colors.cyan[600],
          // leading: IconButton(onPressed: () {}, icon: const Icon(Icons.abc)),
          centerTitle: true,
          bottom: const TabBar(
            indicatorColor: Color.fromARGB(255, 0, 255, 255),
            indicatorWeight: 5,
            unselectedLabelColor: Color.fromARGB(255, 0, 0, 0),
            labelColor: Color.fromARGB(255, 255, 0, 0),
            tabs: [
              Tab(
                icon: Icon(Icons.android),
                child: Text("andorid"),
              ),
              Tab(
                icon: Icon(Icons.apple),
                child: Text("apple"),
              ),
              Tab(
                icon: Icon(Icons.align_vertical_bottom),
                child: Text("hello"),
              )
            ],
          ),
          actions: [
            IconButton(
                onPressed: () {
                  FirebaseAuth.instance.signOut();
                  GoogleSignIn().currentUser == null
                      ? null
                      : GoogleSignIn().disconnect();
                  Navigator.pushReplacement(context,
                      MaterialPageRoute(builder: (context) {
                    return Page1();
                  }));
                },
                icon: const Icon(Icons.exit_to_app)),
            PopupMenuButton(
              color: Colors.red,
              icon: const Icon(
                Icons.laptop_mac_outlined,
                color: Colors.white,
              ),
              itemBuilder: (context) => const [
                PopupMenuItem(
                  value: "islam1",
                  child: Text("data1"),
                ),
                PopupMenuItem(
                  value: "islam2",
                  child: Text("data2"),
                ),
                PopupMenuItem(
                  value: "islam3",
                  child: Text("data3"),
                ),
                PopupMenuItem(
                  value: "islam4",
                  child: Text("data4"),
                )
              ],
            ),
            Builder(builder: (context) {
              return IconButton(
                  onPressed: () {
                    showSearch(context: context, delegate: Customeme());
                  },
                  icon: const Icon(Icons.search));
            })
          ],
        ),
      ),
    );
  }
}

class Customeme extends SearchDelegate {
  List usernamess = [
    "islam 1",
    "islam 2",
    "islam 3",
    "islam 4",
    "islam 5",
    "islam 6",
  ];
  List? filtter;
  @override
  List<Widget>? buildActions(BuildContext context) {
    return [IconButton(onPressed: () {}, icon: const Icon(Icons.search))];
  }

  @override
  Widget? buildLeading(BuildContext context) {
    return IconButton(
        onPressed: () {
          query = "";
          close(context, null);
        },
        icon: const Icon(Icons.close));
  }

  @override
  Widget buildResults(BuildContext context) {
    return Text("Context Is $query");
  }

  @override
  Widget buildSuggestions(BuildContext context) {
    if (query.isEmpty) {
      return ListView.builder(
        itemCount: usernamess.length,
        itemBuilder: (context, index) {
          return InkWell(
            onTap: () => showResults(context),
            child: Card(
              child: Text(
                usernamess[index],
                style: const TextStyle(
                  fontSize: 20,
                ),
              ),
            ),
          );
        },
      );
    } else {
      filtter = usernamess.where((element) => element.contains(query)).toList();
      return ListView.builder(
        itemCount: filtter!.length,
        itemBuilder: (context, index) {
          return InkWell(
            onTap: () {
              showResults(context);
            },
            child: Card(
              child: Text(
                filtter![index],
                style: const TextStyle(
                  fontSize: 20,
                ),
              ),
            ),
          );
        },
      );
    }
  }
}
