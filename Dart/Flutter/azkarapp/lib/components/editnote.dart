// ignore_for_file: avoid_print

import 'package:azkarapp/components/customizedbutton.dart';
import 'package:azkarapp/components/textfromfiled.dart';
import 'package:azkarapp/notehomepage.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

// ignore: must_be_immutable
class EditNote extends StatefulWidget {
  String docid;
  final String oldname;
  EditNote({super.key, required this.docid, required this.oldname});

  @override
  State<EditNote> createState() => _EditNoteeState();
}

// ignore: must_be_immutable
class _EditNoteeState extends State<EditNote> {
  TextEditingController namecontroller = TextEditingController();
  CollectionReference categories =
      FirebaseFirestore.instance.collection('categories');
  GlobalKey<FormState> fm = GlobalKey<FormState>();
  
  
  Future<void> addcategorie(BuildContext context) async {
    // Call the user's CollectionReference to add a new user
    if (fm.currentState!.validate()) {
      try {
        await categories.doc(widget.docid).set({
          'note_name': namecontroller.text,
          'id' : FirebaseAuth.instance.currentUser!.uid
        },SetOptions(merge: true)); 
        // ignore: use_build_context_synchronously
        Navigator.pushAndRemoveUntil(
            // ignore: use_build_context_synchronously
            context,
            MaterialPageRoute(builder: (context) => const NoteHomePage()),
            (route) => false);
      } catch (e) {
        print(e);
      }
    }
  }
  initState() {
    super.initState();
    namecontroller.text = widget.oldname;
  }
  @override
  void dispose() {
    // TODO: implement dispose
    super.dispose();
    namecontroller.dispose();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Edit Note"),
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
                  addcategorie(context);
                },
                title: const Text("Edit Note"),
              )
            ],
          ),
        ),
      ),
    );
  }
}
