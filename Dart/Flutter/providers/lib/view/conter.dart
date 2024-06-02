// ignore_for_file: must_be_immutable


import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:providers/model/serv.dart';

class Counter extends GetView<GeServ> {
  const Counter({super.key});
  // HomeControler controller = Get.put(HomeControler(), permanent: true);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:  Text("1".tr),
        backgroundColor: Colors.indigo,
      ),
      body: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          IconButton(
              onPressed: () {
                controller.increment();
              },
              icon: const Icon(
                Icons.add,
              )),
          GetX<GeServ>(
              builder: (controller) => Text("${controller.conter.value}")),
          IconButton(
              onPressed: () {
                controller.decrement();
              },
              icon: const Icon(
                Icons.remove,
              )),
        ],
      ),
    );
  }
}

