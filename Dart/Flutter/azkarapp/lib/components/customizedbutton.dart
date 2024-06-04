// ignore_for_file: non_constant_identifier_names, must_be_immutable

import 'package:flutter/material.dart';

class CustumizedButton extends StatelessWidget {
  CustumizedButton(
      {super.key,
      required this.Function_to_use,
      required this.title,});
  VoidCallback? Function_to_use;
  late Widget title;

  @override
  Widget build(BuildContext context) {
    return MaterialButton(
      onPressed: Function_to_use,
      color: Colors.blue,
      minWidth: double.infinity,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(40)),
      height: 50,
      child: title,
    );
  }
}

void main(List<String> args) {
}
