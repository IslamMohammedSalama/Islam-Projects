import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:providers/main.dart';

class Mdw extends GetMiddleware{
  @override
  int? get priority => 2;
  @override
  RouteSettings? redirect(String? route) {
    if (sharedPreferences.getString("login") != null) return const RouteSettings(name: "/logout");
    if (sharedPreferences.getString("role") == "admin") return const RouteSettings(name: "/logoutasadmin");
    super.redirect(route);
    return null;
  }
}

class SMdw extends GetMiddleware {
  @override 
  int? get priority => 1;
  @override
  RouteSettings? redirect(String? route) {

    if (sharedPreferences.getString("role") == "sudoadmin") {
      return const RouteSettings(name: "/logoutassudoadmin");
    }
    super.redirect(route);
    return null;
  }
}
