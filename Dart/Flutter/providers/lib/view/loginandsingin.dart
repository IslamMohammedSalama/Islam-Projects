import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:providers/main.dart';

class Login extends StatelessWidget {
  const Login({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:  Text("1".tr),
      ),
      body: Center(
          child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          MaterialButton(
            child: const Text("Login"),
            onPressed: () {
              sharedPreferences.setString("login", "1");
              Get.offAndToNamed("/logout");
            },
          ),
          MaterialButton(
            child: const Text("LoginAsAdmin"),
            onPressed: () {
              sharedPreferences.setString("role", "admin");
              Get.offAndToNamed("/logoutasadmin");
            },
            
          ),          MaterialButton(
            child: const Text("LoginAssudo"),
            onPressed: () {
              sharedPreferences.setString("role", "sudoadmin");
              Get.offAndToNamed("/logoutassudoadmin");
            },)
        ],
      )),
    );
  }
}

class Logout extends StatelessWidget {
  const Logout({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("data"),
      ),
      body: Center(
          child: MaterialButton(
        child: const Text("Logout"),
        onPressed: () {

          sharedPreferences.clear();
          Get.offAndToNamed("/login");
        },
      )),
    );
  }
}
