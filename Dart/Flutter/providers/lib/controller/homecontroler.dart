// ignore_for_file: avoid_print

import 'package:get/get.dart';

class HomeControler extends GetxController {
  // late String name;
  int conter = 0;
  void increment() {
    conter++;
    update();
  }

  void decrement() {
    conter--;
    update();
  }

  @override
  void onInit() {
    // name = Get.arguments["name"];
    print("init complate");
    super.onInit();
  }

  @override
  void onReady() {
    print("redey to use");
    super.onReady();
  }
}

class Coter extends GetxController {
  late String name;
  late String cr;
  late String pr;
  @override
  void onInit() {
    name = Get.arguments["name"];
    cr = Get.routing.current;
    pr = Get.previousRoute;
    super.onInit();
  }
}
