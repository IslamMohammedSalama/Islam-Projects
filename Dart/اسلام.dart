class islam {
  int? a;
  String islameat() {
    return "  islam is eatting ";
  }
}

class hashem extends islam {
  @override
  String islameat() {
    return "  hashem is eatting ";
  }
}

void main() {
  hashem l = new hashem();
  print("${l.islameat()}");
}
