// ignore_for_file: must_be_immutable, avoid_print, use_build_context_synchronously

import 'package:azkarapp/auth/singin.dart';
import 'package:azkarapp/components/textfromfiled.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class Page1 extends StatelessWidget {
  Page1({super.key});
  TextEditingController email = TextEditingController();
  TextEditingController password = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Form(
        child: SafeArea(
          child: Container(
            padding: const EdgeInsets.all(10),
            child: ListView(children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const SizedBox(
                    height: 50,
                  ),
                  Center(
                    child: Container(
                      alignment: Alignment.center,
                      decoration: const BoxDecoration(
                          borderRadius: BorderRadius.all(Radius.circular(70)),
                          color: Color.fromARGB(255, 139, 200, 250)),
                      padding: const EdgeInsets.all(10),
                      width: 70,
                      height: 70,
                      child: Image.asset(
                        "assets/icons/lunchericon.png",
                        width: 50,
                        height: 50,
                      ),
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  const Text(
                    "Login ",
                    style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
                  ),
                  const Text("LogIn To Continue"),
                  const SizedBox(
                    height: 20,
                  ),
                  const Text("Email"),
                  CustomizedTextField(
                      controller: email,
                      hintText: "Enter Email",
                      obscureText: false),
                  const SizedBox(
                    height: 10,
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  const Text("Password"),
                  const SizedBox(
                    height: 10,
                  ),
                  CustomizedTextField(
                      controller: password,
                      hintText: "Enter Password",
                      obscureText: true),
                  const SizedBox(
                    height: 20,
                  ),
                  const Align(
                    alignment: Alignment.topRight,
                    child: Text(
                      "Forget Password ?",
                      style: TextStyle(color: Colors.blue),
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  MaterialButton(
                    onPressed: () async {
                      print("${email.text} => ${password.text}");
                      try {
                        final credential = await FirebaseAuth.instance
                            .signInWithEmailAndPassword(
                                email: email.text, password: password.text);
                      } on FirebaseAuthException catch (e) {
                        if (e.code == 'user-not-found') {
                          print('No user found for that email.');
                        } else if (e.code == 'wrong-password') {
                          print('Wrong password provided for that user.');
                        }
                      }
                    },
                    color: Colors.blue,
                    minWidth: double.infinity,
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(40)),
                    height: 50,
                    child: const Text("Login"),
                  ),
                  const SizedBox(height: 20),
                  const Align(child: Text("Or Login With ")),
                  Row(
                      // crossAxisAlignment: CrossAxisAlignment.center,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        IconButton(
                          onPressed: () {},
                          icon: const Icon(Icons.facebook),
                        ),
                        IconButton(
                          onPressed: () {},
                          icon: const Icon(Icons.apple),
                        ),
                        IconButton(
                          onPressed: () {},
                          icon: const Icon(Icons.flutter_dash),
                        )
                      ]),
                  const SizedBox(height: 20),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Text(
                        "Don't have an account ? ",
                      ),
                      InkWell(
                          onTap: () {
                            Navigator.pushReplacement(
                                context,
                                MaterialPageRoute(
                                    builder: (context) => SingIn()));
                          },
                          child: const Text(
                            "Register",
                            style: TextStyle(color: Colors.blue),
                          ))
                    ],
                  )
                ],
              )
            ]),
          ),
        ),
      ),
    );
  }
}
