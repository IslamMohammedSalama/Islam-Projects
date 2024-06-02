import 'package:get/get.dart';
import 'package:providers/controller/homecontroler.dart';

class Binders implements Bindings {
  @override
  void dependencies() {
    Get.put( HomeControler(), permanent: true);

  }
}