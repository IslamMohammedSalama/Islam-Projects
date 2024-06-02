// ignore_for_file: use_build_context_synchronously

import 'package:azkarapp/auth/page.dart';
import 'package:azkarapp/components/addnote.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';

class NoteHomePage extends StatelessWidget {
  const NoteHomePage({super.key});
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
      body: GridView(
          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              mainAxisSpacing: 10,
              crossAxisSpacing: 10,
              mainAxisExtent: 150,
              crossAxisCount: 2),
          children: const [
            Card(
              color: Colors.blue,
              child: Icon(Icons.folder),
            ),
            Card(
              color: Colors.blue,
              child: Icon(Icons.person),
            ),
            Card(
              color: Colors.blue,
              child: Icon(Icons.contact_mail_sharp),
            ),
          ]),
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
              GoogleSignIn().currentUser != null
                  ? GoogleSignIn().disconnect()
                  : null;
              await FirebaseAuth.instance.signOut();
              Navigator.pushReplacement(
                context,
                MaterialPageRoute(
                  builder: (context) {
                    return Page1();
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
