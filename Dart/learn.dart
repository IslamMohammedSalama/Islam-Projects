import 'dart:io';

double get_result(double num1, double num2, String? operator) {
  double result = 0;
  if (operator == "+") {
    result = num1 + num2;
  } else if (operator == "-") {
    result = num1 - num2;
  } else if (operator == "*") {
    result = num1 * num2;
  } else if (operator == "/") {
    if (num2 == 0) {
      print("Error: Division by zero");
      return 0;
    } else {
      result = num1 / num2;}
  } else {
    print("Error: Invalid operator");
    return 0;
  }
  return result;
}

void main() {

  bool loop = true ; 
  while (loop) {

    stdout.write("Enter the First Number: ");
    String? input1 = stdin.readLineSync();
    double num1 = double.parse(input1!);

    stdout.write("Enter The Second Number: ");
    String? input2 = stdin.readLineSync();
    double num2 = double.parse(input2!);

    stdout.write("Enter The Operator (+, -, *, /): ");
    String? input3 = stdin.readLineSync();

    print("Result is ${get_result(num1, num2, input3)}");

      while (loop) {
    try {
      stdout.write("Do you repeat that (y, yes, n, no)? ");
      String? repeat = stdin.readLineSync()?.toLowerCase();

      if (repeat == "y" || repeat == "yes") {
        break;
      } else if (repeat == "n" || repeat == "no") {
        loop = false;
        break;
      } else {
        throw FormatException("Invalid input. Please input only (y, yes, n, no)");
      }
    } on FormatException catch (e) {
      print(e.message);
    }
  }}}

