// ignore_for_file: must_be_immutable, avoid_print, use_build_context_synchronously

import 'package:azkarapp/auth/singin.dart';
import 'package:azkarapp/components/customizedbutton.dart';
import 'package:azkarapp/components/textfromfiled.dart';
import 'package:azkarapp/homepage.dart';
import 'package:azkarapp/notehomepage.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';

class Page1 extends StatelessWidget {
  Page1({super.key});
  TextEditingController email = TextEditingController();
  TextEditingController password = TextEditingController();
  final GlobalKey<FormState> _formstate = GlobalKey<FormState>();
  Future signInWithGoogle() async {
    // Trigger the authentication flow
    final GoogleSignInAccount? googleUser = await GoogleSignIn().signIn();
    if (googleUser == null) return;

    // Obtain the auth details from the request
    final GoogleSignInAuthentication googleAuth =
        await googleUser.authentication;

    // Create a new credential
    final credential = GoogleAuthProvider.credential(
      accessToken: googleAuth.accessToken,
      idToken: googleAuth.idToken,
    );

    // Once signed in, return the UserCredential
    await FirebaseAuth.instance.signInWithCredential(credential);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Form(
        key: _formstate,
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
                  Align(
                    alignment: Alignment.topRight,
                    child: InkWell(
                      onTap: () {
                        if (email.text.isEmpty) {
                          showDialog(
                              context: context,
                              builder: (context) => const AlertDialog(
                                    title: Text("Error"),
                                    content: Text(
                                        "Enter Email and Press forget passweord"),
                                  ));
                        } else {
                          FirebaseAuth.instance.sendPasswordResetEmail(email: email.text);
                          showDialog(
                              context: context,
                              builder: (context) => const AlertDialog(
                                    title: Text("Reset Password"),
                                    content: Text(
                                        "Go To Gmail TO Reset The Password"),
                                  ));
                        }
                      },
                      child: const Text(
                        "Forget Password ?",
                        style: TextStyle(color: Colors.blue),
                      ),
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                   CustumizedButton(Function_to_use: ()async{
                          if (_formstate.currentState!.validate()) {
                        print("${email.text} => ${password.text}");
                        try {
                          await FirebaseAuth.instance
                              .signInWithEmailAndPassword(
                                  email: email.text, password: password.text);
                          Navigator.pushAndRemoveUntil(
                              context,
                              MaterialPageRoute(
                                builder: (context) => const Homepage(),
                              ),
                              (route) => false);
                        } on FirebaseAuthException catch (e) {
                          print(e.code);
                          showDialog(
                            context: context,
                            builder: (context) => AlertDialog(
                              title: const Text("Error"),
                              content: Text(e.code),
                            ),
                          );

                          if (e.code == 'user-not-found') {
                            print('No user found for that email. ');
                          } else if (e.code == 'wrong-password') {
                            print('Wrong password provided for that user.');
                          } else if (e.code == 'invalid-email') {
                            print("inv em");
                          } else if (e.code == 'user-disabled') {
                            print('The user account has been disabled.');
                          }
                        }
                      } else {
                        print("not valid");
                      }
  },title: "Login"),
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
                          onPressed: () async {
                            await signInWithGoogle();
                            Navigator.of(context).pushReplacement(MaterialPageRoute(
                                builder: (context) => const  NoteHomePage()));
                          },
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
