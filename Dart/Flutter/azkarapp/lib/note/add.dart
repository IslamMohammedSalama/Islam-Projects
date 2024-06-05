// ignore_for_file: avoid_print

import 'package:azkarapp/components/customizedbutton.dart';
import 'package:azkarapp/components/textfromfiled.dart';
import 'package:azkarapp/note/view.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

class AddSubNote extends StatefulWidget {
  final String subdocid;
  const AddSubNote({super.key, required this.subdocid});

  @override
  State<AddSubNote> createState() => _AddSubNoteState();
}

// ignore: must_be_immutable
class _AddSubNoteState extends State<AddSubNote> {
  TextEditingController notecontroller = TextEditingController();

  GlobalKey<FormState> fm = GlobalKey<FormState>();

  Future<void> addnote(BuildContext context) async {  CollectionReference collectionnotes =
      FirebaseFirestore.instance.collection('categories').doc(widget.subdocid).collection('note');
    // Call the user's CollectionReference to add a new user
    if (fm.currentState!.validate()) {
      try {
        DocumentReference docRef = await collectionnotes.add({
          'note_name': notecontroller.text, // John Doe
        });
        // ignore: use_build_context_synchronously
        Navigator.pushReplacement(
            context,
            MaterialPageRoute(builder: (context) =>  ViewNotes(categorieid: widget.subdocid,)),
            );
      } catch (e) {
        print(e);
      }
    }
  }
  @override
  void dispose() {
    super.dispose();
    notecontroller.dispose();

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Add Note"),
        centerTitle: true,
      ),
      body: Form(
        key: fm,
        child: Padding(
          padding: const EdgeInsets.all(10),
          child: ListView(
            children: [
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 10),
                child: CustomizedTextField(
                    controller: notecontroller,
                    hintText: "Enter Your Note Name",
                    obscureText: false),
              ),
              CustumizedButton(
                Function_to_use: () {
                  addnote(context);
                },
                title: const Text("Add Note"),
              )
            ],
          ),
        ),
      ),
    );
  }
}


/* 

  CollectionReference categories = FirebaseFirestore.instance.collection('categories');

  Future<void> addUser(String fullName, String company, int age) {
    // Call the user's CollectionReference to add a new user
    return categories
        .add({
          'full_name': fullName, // John Doe
          'company': company, // Stokes and Sons
          'age': age // 42
        })
        .then((value) => print("categoried Added"))
        .catchError((error) => print("Failed to add categoried: $error"));
  }
 */