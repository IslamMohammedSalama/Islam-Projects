// ignore_for_file: must_be_immutable

import 'package:get/get.dart';
import 'package:flutter/material.dart';
import 'package:providers/locate/locate.dart';
import 'package:providers/locate/locate_cont.dart';
import 'package:providers/model/bind.dart';
import 'package:providers/model/mdw.dart';
import 'package:providers/model/serv.dart';
import 'package:providers/view/admin.dart';
import 'package:providers/view/loginandsingin.dart';
import 'package:providers/view/page2.dart';
import 'package:providers/view/page3.dart';
import 'view/homepage.dart';
import 'package:shared_preferences/shared_preferences.dart';

late SharedPreferences sharedPreferences;
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await initserv();
  sharedPreferences = await SharedPreferences.getInstance();

  runApp( MyApp());
}

Future initserv() async {
  await Get.putAsync(() => GeServ().init(), permanent: true);
}

class MyApp extends StatelessWidget {
   MyApp({super.key});
  LocateControler lcs =    Get.put(LocateControler());
  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      locale:lcs.InitLocate,
      translations: Locates(),
      // home:const HomePage(),
      initialRoute: "/",
      debugShowCheckedModeBanner: false,
      getPages: [
        GetPage(name: "/", page: () => const HomePage(), binding: Binders()),
        GetPage(name: "/page2", page: () => Page2()),
        GetPage(name: "/page3", page: () => const Page3()),
        GetPage(
            name: "/login",
            page: () => const Login(),
            middlewares: [SMdw(), Mdw()]),
        GetPage(name: "/logout", page: () => const Logout()),
        GetPage(name: "/logoutasadmin", page: () => const LogoutAsAdmin()),
        GetPage(name: "/logoutassudoadmin", page: () => const SudoAdmin()),
      ],
    );
  }
}
