// ignore_for_file: avoid_print

import 'package:azkarapp/components/customizedbutton.dart';
import 'package:azkarapp/components/textfromfiled.dart';
import 'package:azkarapp/note/view.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

// ignore: must_be_immutable
class EditSubNote extends StatefulWidget {
  String docid;
  String categoriid;
  final String oldname;
  EditSubNote({super.key, required this.docid, required this.oldname, required this.categoriid});

  @override
  State<EditSubNote> createState() => _EditSubNoteeState();
}

// ignore: must_be_immutable
class _EditSubNoteeState extends State<EditSubNote> {
  TextEditingController namecontroller = TextEditingController();

  GlobalKey<FormState> fm = GlobalKey<FormState>();

  Future<void> renamenote(BuildContext context) async {  CollectionReference categories =
      FirebaseFirestore.instance.collection('categories').doc(widget.categoriid).collection('note');
    // Call the user's CollectionReference to add a new user
    if (fm.currentState!.validate()) {
      try {
        await categories.doc(widget.docid).set({
          'note_name': namecontroller.text,
        }, SetOptions(merge: true));
        // ignore: use_build_context_synchronously
        Navigator.pushReplacement(
            // ignore: use_build_context_synchronously
            context,
            MaterialPageRoute(builder: (context) =>  ViewNotes(categorieid: widget.categoriid,)),
            );
      } catch (e) {
        print(e);
      }
    }
  }

  @override
  void initState() {
    super.initState();
    namecontroller.text = widget.oldname;
  }

  @override
  void dispose() {
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
                  renamenote(context);
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
