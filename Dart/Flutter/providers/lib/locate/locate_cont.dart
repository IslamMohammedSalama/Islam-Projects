// ignore_for_file: non_constant_identifier_names

import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:providers/main.dart';

class LocateControler extends GetxController{
  Locale? InitLocate = sharedPreferences.getString("locate")==null?Get.deviceLocale : Locale(sharedPreferences.getString("locate")!) ;
  void chl(String locate){
    sharedPreferences.setString("locate", locate);
    Get.updateLocale(Locale(locate));
  }
}