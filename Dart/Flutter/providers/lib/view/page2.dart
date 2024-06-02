import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:providers/controller/homecontroler.dart';

class Page2 extends StatelessWidget {
  Page2({super.key});
  final cont = Get.put(Coter());
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.blue,
          title: Text("1".tr),
        ),
        body: Center(
            child: Column(
          children: [
            Text(cont.name),
            MaterialButton(
                child: const Text("Back"),
                onPressed: () {
                  Get.back();
                }),
            MaterialButton(
                child: const Text("Replace"),
                onPressed: () {
                  Get.toNamed("/page3");
                })
          ],
        )));
  }
}
