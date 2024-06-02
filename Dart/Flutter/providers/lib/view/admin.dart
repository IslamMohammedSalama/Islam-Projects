import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:providers/main.dart';


class LogoutAsAdmin extends StatelessWidget {
  const LogoutAsAdmin({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("data"),
      ),
      body: Center(
          child: MaterialButton(
        child: const Text("LogOutAsAdmin"),
        onPressed: () {
          sharedPreferences.clear();
          Get.offAndToNamed("/login");
        },
      )),
    );
  }
}



class SudoAdmin extends StatelessWidget {
  const SudoAdmin({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:  Text("1".tr),
      ),
      body: Center(
          child: MaterialButton(
        child: const Text("LogOutAsSudoAdmin"),
        onPressed: () {
          sharedPreferences.clear();
          Get.offAndToNamed("/login");
        },
      )),
    );
  }
}
