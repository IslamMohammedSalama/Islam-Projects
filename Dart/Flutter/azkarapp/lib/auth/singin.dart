// ignore_for_file: must_be_immutable, use_build_context_synchronously, avoid_print

import 'package:azkarapp/auth/page.dart';
import 'package:azkarapp/components/textfromfiled.dart';
import 'package:azkarapp/notehomepage.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:azkarapp/components/customizedbutton.dart';
import 'package:quickalert/models/quickalert_type.dart';
import 'package:quickalert/widgets/quickalert_dialog.dart';
class SingIn extends StatefulWidget {
  const SingIn({super.key});

  @override
  State<SingIn> createState() => _SingInState();
}

class _SingInState extends State<SingIn> {
  TextEditingController username = TextEditingController();
  TextEditingController email = TextEditingController();
  TextEditingController password = TextEditingController();
  TextEditingController confpass = TextEditingController();
  final GlobalKey<FormState> _formstate = GlobalKey<FormState>();
  bool _isloading = false;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Form(
        key: _formstate,
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
              CustumizedButton(
                Function_to_use: () async {
                  if (_formstate.currentState!.validate()) {
                    _isloading = true;
                    setState(() {});
                    try {
                      final credential = await FirebaseAuth.instance
                          .createUserWithEmailAndPassword(
                        email: email.text,
                        password: password.text,
                      );
                      Navigator.pushReplacement(
                          context,
                          MaterialPageRoute(
                              builder: (context) =>  const NoteHomePage()));
                    } on FirebaseAuthException catch (e) {
                      print(e);
                      if (e.code == 'weak-password') {
                        print('The password provided is too weak.');
                        QuickAlert.show(
                            context: context,
                            title: "Error",
                            text: "The password provided is too weak.",
                            type: QuickAlertType.error);
                            _isloading = false;
                            setState(() {});
                      } else if (e.code == 'email-already-in-use') {
                        print('The account already exists for that email.');
                        QuickAlert.show(
                            context: context,
                            title: "Error",
                            text: "The account already exists for that email.",
                            type: QuickAlertType.error);
                             _isloading = false;
                        setState(() {});
                      }
                    } catch (e) {
                      print(e);
                    }
                     _isloading = false;
                    setState(() {});
                  }
                },
                title: _isloading
                    ? const Center(
                        child: CircularProgressIndicator(
                        color: Colors.white,
                      ))
                    : const  Text("Register"),
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
                            MaterialPageRoute(builder: (context) =>const Page1()));
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
