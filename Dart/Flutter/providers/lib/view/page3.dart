import 'package:flutter/material.dart';
import 'package:get/get.dart';

class Page3 extends StatelessWidget {
  const Page3({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title:  Text("1".tr),
          backgroundColor: Colors.green,
        ),
        body: Center(
            child: MaterialButton(
                child: const Text("replace"),
                onPressed: () {
                  Get.offAllNamed("/page2");
                })));
  }
}
