import 'package:get/get.dart';
import 'package:shared_preferences/shared_preferences.dart';

class GeServ extends GetxService {
  late SharedPreferences shares;
  RxInt conter = 0.obs;

  Future<GeServ> init() async {
    shares = await SharedPreferences.getInstance();
    conter.value = shares.getInt("conter") ?? 0;
    return this;
  }

  increment() {
    conter++;
    shares.setInt("conter", conter.value);
  }
  decrement(){
    conter--;
    shares.setInt("conter", conter.value);
  }
}
