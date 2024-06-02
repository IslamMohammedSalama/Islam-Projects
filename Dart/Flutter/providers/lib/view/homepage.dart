// ignore_for_file: avoid_print

import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:providers/locate/locate_cont.dart';
import 'package:providers/view/conter.dart';
import 'package:providers/view/p2.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});
  @override
  Widget build(BuildContext context) {
    LocateControler lc = Get.find();
    return Scaffold(
      appBar: AppBar(
        title: Text("1".tr),
        backgroundColor: Colors.red,
      ),
      body: Center(
        child: ListView(
          children: [
            MaterialButton(
              onPressed: () {
                Get.toNamed(
                  "/page2",
                  arguments: {"name": "islam"},
                );
              },
              child: const Text("Click me"),
            ),
            MaterialButton(
              onPressed: () {
                Get.back();
              },
              child: const Text("Back"),
            ),
            MaterialButton(
              onPressed: () {
                Get.to(() => const Counter());
              },
              child: const Text("Go To Counter"),
            ),
            MaterialButton(
              onPressed: () {
                Get.to(() => P2());
              },
              child: const Text("Go To P2"),
            ),
            MaterialButton(
              onPressed: () {
                lc.chl("ar");
              },
              child: const Text("Change To Ar"),
            ),
            MaterialButton(
              onPressed: () {
                lc.chl("en");
              },
              child: const Text("Change To En"),
            ),
            MaterialButton(
              onPressed: () {
                Get.defaultDialog(
                    title: "HiDilog",
                    content: Form(
                      child: TextFormField(
                          autocorrect: true,
                          decoration: const InputDecoration(
                              border: OutlineInputBorder(),
                              hintText: "Enter Your Name",
                              prefixIcon: Icon(Icons.person))),
                    ),
                    confirm: MaterialButton(
                      onPressed: () {},
                      child: const Text("Submit"),
                    ),
                    cancel: MaterialButton(
                      onPressed: () {
                        print("Cancled");
                        Get.back();
                      },
                      child: const Text("Cancel"),
                    ));
              },
              child: const Text("Show Dilog"),
            ),
            MaterialButton(
                onPressed: () {
                  Get.snackbar(
                    "Hi",
                    "Show Snack Bar",
                    backgroundColor: Colors.green,
                    snackPosition: SnackPosition.BOTTOM,
                    borderRadius: 0,
                    margin: const EdgeInsets.all(0),
                    maxWidth: 200,
                    colorText: Colors.amber,
                    showProgressIndicator: true,
                    progressIndicatorBackgroundColor: Colors.black,
                    borderColor: Colors.red,
                    borderWidth: 2,
                    barBlur: 50.0,
                    boxShadows: [
                      const BoxShadow(
                          color: Color.fromARGB(255, 0, 255, 17),
                          blurRadius: 10.0,
                          offset: Offset(1.0, 1.0),
                          spreadRadius: 10.0,
                          blurStyle: BlurStyle.normal),
                    ],
                    animationDuration: const Duration(seconds: 10),
                    duration: const Duration(seconds: 10),
                  );
                },
                child: const Text("Show Snack Bar")),
            MaterialButton(
              onPressed: () {
                Get.bottomSheet(
                    SizedBox(
                      height: 200,
                      child: ListView(
                        children: [
                          MaterialButton(
                            onPressed: () {
                              print(Get.isBottomSheetOpen);
                            },
                            child: const Text("Is Opend"),
                          ),
                          const Text(
                            "Hello",
                            textAlign: TextAlign.center,
                          ),
                          MaterialButton(
                            onPressed: () {
                              Get.back();
                            },
                            child: const Text("Close Bottom Draweer"),
                          ),
                        ],
                      ),
                    ),
                    backgroundColor: Colors.white,
                    enterBottomSheetDuration: const Duration(seconds: 10),
                    exitBottomSheetDuration: const Duration(seconds: 10),
                    enableDrag: false,
                    isDismissible: false);
              },
              child: const Text("Bottom Draweer"),
            ),
            MaterialButton(
              onPressed: () {
                print(Get.isSnackbarOpen);
                print(Get.isBottomSheetOpen);
              },
              child: const Text("Is Opend"),
            ),
            MaterialButton(
              onPressed: () {
                print(Get.height);
              },
              child: const Text("Is Opend"),
            )
          ],
        ),
      ),
    );
  }
}
