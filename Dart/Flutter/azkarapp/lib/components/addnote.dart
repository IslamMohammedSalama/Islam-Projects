// ignore_for_file: avoid_print

import 'package:azkarapp/components/customizedbutton.dart';
import 'package:azkarapp/components/textfromfiled.dart';
import 'package:azkarapp/notehomepage.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class AddNote extends StatefulWidget {
  const AddNote({super.key});

  @override
  State<AddNote> createState() => _AddNoteState();
}



// ignore: must_be_immutable
class _AddNoteState extends State<AddNote> {

  TextEditingController namecontroller = TextEditingController();
  CollectionReference categories =
      FirebaseFirestore.instance.collection('categories');
  GlobalKey<FormState> fm = GlobalKey<FormState>();

  Future<void> renamecategorie(BuildContext context) async {
    // Call the user's CollectionReference to add a new user
    if (fm.currentState!.validate()) {
      try {
        DocumentReference docRef = await categories.add({
          'note_name': namecontroller.text, // John Doe
          'id' : FirebaseAuth.instance.currentUser!.uid
        });
        // ignore: use_build_context_synchronously
        Navigator.pushAndRemoveUntil(context,MaterialPageRoute(builder: (context) => const NoteHomePage()), (route) => false);
      } catch (e) {
        print(e);
      }
    }
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
                    controller: namecontroller,
                    hintText: "Enter Your Note Name",
                    obscureText: false),
              ),
              CustumizedButton(
                Function_to_use: () {
                  renamecategorie(context);

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