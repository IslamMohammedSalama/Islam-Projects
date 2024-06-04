// ignore_for_file: use_build_context_synchronously, avoid_print

import 'package:azkarapp/auth/page.dart';
import 'package:azkarapp/components/addnote.dart';
 import 'package:azkarapp/components/editnote.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';
import 'package:quickalert/models/quickalert_type.dart';
import 'package:quickalert/widgets/quickalert_dialog.dart';

class NoteHomePage extends StatefulWidget {
  const NoteHomePage({super.key});

  @override
  State<NoteHomePage> createState() => _NoteHomePageState();
}

// ignore: must_be_immutable
class _NoteHomePageState extends State<NoteHomePage> {
  List data = [];
  bool islooading = true;
  readDate() async {
    QuerySnapshot querySnapshot =
        await FirebaseFirestore.instance.collection("categories").where('id' , isEqualTo: FirebaseAuth.instance.currentUser!.uid).get();
    data.addAll(querySnapshot.docs);
    islooading = false;
    setState(() {});
  }

  @override
  void initState() {
    readDate();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(context, MaterialPageRoute(builder: (context) {
            return const AddNote();
          }));
        },
        child: const Icon(Icons.add),
      ),
      body: islooading == true
          ? const Center(
              child: CircularProgressIndicator(
              color: Colors.blue,
            ))
          : GridView.builder(
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  mainAxisSpacing: 10,
                  crossAxisSpacing: 10,
                  mainAxisExtent: 150,
                  crossAxisCount: 2),
              itemCount: data.length,
              itemBuilder: (context, index) {
                return InkWell(
                  borderRadius: BorderRadius.circular(10),
                  onLongPress: () => QuickAlert.show(
                      context: context,
                      showCancelBtn: true,
                    
                      type: QuickAlertType.warning,
                      title: "What you want to do?",
                      confirmBtnText: "Edit",
                      
                      cancelBtnText: "Remove",
                      
                      confirmBtnColor: Colors.blue,
                      onCancelBtnTap: () async{                        await FirebaseFirestore.instance
                            .collection("categories")
                            .doc(data[index].id)
                            .delete();
                        Navigator.pushAndRemoveUntil(context,
                            MaterialPageRoute(builder: (context) {
                          return const NoteHomePage();
                        }), (route) => false);
                        
                      },
                      onConfirmBtnTap: ()  {
Navigator.push(context, MaterialPageRoute(builder: (context) {
  return  EditNote(docid: data[index].id,oldname: data[index]["note_name"],);
}));
                      }),
                  child: Card(
                    color: Colors.blue,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        const Icon(
                          Icons.folder,
                          color: Color.fromARGB(255, 65, 65, 65),
                          size: 80,
                        ),
                        Center(
                          child: Text(
                            data[index]["note_name"],
                            style: const TextStyle(fontSize: 25),
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              }),
      appBar: AppBar(
        centerTitle: true,
        backgroundColor: Colors.blueGrey,
        elevation: 0,
        actions: [ 
          const Icon(Icons.search),
          const SizedBox(width: 10),
          const Icon(Icons.more_vert),
          const SizedBox(width: 10),
          IconButton(
            onPressed: () async {
              GoogleSignIn().disconnect();
              await FirebaseAuth.instance.signOut();
              Navigator.pushReplacement(
                context,
                MaterialPageRoute(
                  builder: (context) {
                    return const Page1();
                  },
                ),
              );
            },
            icon: const Icon(Icons.exit_to_app),
          )
        ],
        title: const Text("Note App"),
      ),
    );
  }
}
