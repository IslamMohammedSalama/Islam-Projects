import 'package:azkarapp/components/customizedbutton.dart';
import 'package:azkarapp/components/textfromfiled.dart';
import 'package:flutter/material.dart';

class AddNote extends StatelessWidget {
  const AddNote({super.key});

  @override
  Widget build(BuildContext context) {
    TextEditingController namecontroller = TextEditingController();
    return Scaffold(
      appBar: AppBar(
        title: const Text("Add Note"),
        centerTitle: true,
      ),
      body: Form(
        child: Padding(
          padding: const EdgeInsets.all(10),
          child: ListView(
            children: [
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 10),
                child: CustomizedTextField(
                    controller: namecontroller,
                    hintText: "Enter Your Note Name",
                    obscureText: false),
              ),
                  CustumizedButton(Function_to_use: (){}, title: "Add Note",)
            ],
          ),
        ),
      ),
    );
    
  }
}