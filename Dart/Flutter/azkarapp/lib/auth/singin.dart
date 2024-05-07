// ignore_for_file: must_be_immutable, avoid_print, use_build_context_synchronously

import 'package:azkarapp/auth/page.dart';
import 'package:azkarapp/components/textfromfiled.dart';
import 'package:azkarapp/homepage.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class SingIn extends StatelessWidget {
  SingIn({super.key});
  TextEditingController username = TextEditingController();
  TextEditingController email = TextEditingController();
  TextEditingController password = TextEditingController();
  TextEditingController confpass = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Form(
        child: Container(
          padding: const EdgeInsets.all(10),
          child: SafeArea(
            child: ListView(children: [
              const SizedBox(
                height: 40,
              ),
              const Text(
                "Create A New Account",
                style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
              ),
              const SizedBox(
                height: 20,
              ),
              const Text(
                "Your User Name",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              CustomizedTextField(
                  controller: username,
                  hintText: "Enter Your User Name",
                  obscureText: false),
              const SizedBox(
                height: 20,
              ),
              const Text(
                "Your Email",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              CustomizedTextField(
                  controller: email,
                  hintText: "Enter Your Email",
                  obscureText: false),
              const SizedBox(
                height: 20,
              ),
              const Text(
                "Your Password",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              CustomizedTextField(
                  controller: password,
                  hintText: "Enter Your Password",
                  obscureText: true),
              const SizedBox(
                height: 20,
              ),
              const Text(
                "Confirm Password",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              CustomizedTextField(
                  controller: confpass,
                  hintText: "Confirm Password",
                  obscureText: false),
              const SizedBox(
                height: 20,
              ),
              MaterialButton(
                onPressed: () async {
                  try {
                    final credential = await FirebaseAuth.instance.createUserWithEmailAndPassword(
                      email: email.text,
                      password: password.text,
                    );
                    Navigator.pushReplacement(
                        context,
                        MaterialPageRoute(
                            builder: (context) => const homepage()));
                  } on FirebaseAuthException catch (e) {
                    print("sdfas");
                    if (e.code == 'weak-password') {
                      print('The password provided is too weak.');
                      Navigator.pushReplacement(
                          context,
                          MaterialPageRoute(
                              builder: (context) => const homepage()));
                    } else if (e.code == 'email-already-in-use') {
                      print('The account already exists for that email.');
                    }
                  } catch (e) {
                    print(e);
                  }
                },
                color: Colors.cyan,
                shape: const RoundedRectangleBorder(
                    borderRadius: BorderRadius.all(Radius.circular(30))),
                child: const Text("Register"),
              ),
              const SizedBox(height: 20),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text(
                    "Have An Account? ",
                  ),
                  InkWell(
                      onTap: () {
                        Navigator.pushReplacement(context,
                            MaterialPageRoute(builder: (context) => Page1()));
                      },
                      child: const Text(
                        "Login",
                        style: TextStyle(color: Colors.blue),
                      ))
                ],
              )
            ]),
          ),
        ),
      ),
    );
  }
}
