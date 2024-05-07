// ignore_for_file: must_be_immutable

import 'package:flutter/material.dart';


class CustomizedTextField extends StatelessWidget {
    CustomizedTextField(
      {super.key,
      required this.controller,
      required this.hintText,
      required this.obscureText});
  TextEditingController controller;
  String hintText;
  bool obscureText;
  @override
  Widget build(BuildContext context) {
    if (obscureText) {
      return TextFormField(
        obscureText: obscureText,
        controller: controller,
        decoration: InputDecoration(
          
          border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(40),
              borderSide: BorderSide.none),
          hintText: hintText,
          filled: true,
          fillColor: Colors.grey[300],
          enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(40),
              borderSide: BorderSide.none),
        ),
      );
    } else {
      return TextField(
        obscureText: obscureText,
        controller: controller,
        decoration: InputDecoration(
          border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(40),
              borderSide: BorderSide.none),
          hintText: hintText,
          filled: true,
          fillColor: Colors.grey[300],
          enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(40),
              borderSide: BorderSide.none),
        ),
      );
    }
  }
}
