import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:providers/controller/homecontroler.dart';
import 'package:providers/model/serv.dart';

class P2 extends StatelessWidget {
  P2({super.key});
  final controller = Get.lazyPut(((() => HomeControler())));

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
          child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          GetX<GeServ>(
              builder: (contrller) => Text("${contrller.conter}")),
          MaterialButton(
            onPressed: () {
              Get.back();
            },
            child: const Text("islam"),
          )
        ],
      )),
    );
  }
}
