// Test Case 1
let num1 = 9; // "009"

if (num1 < 10 && num1 < 100) {
	console.log(parseInt(`00${num1}`));
}

// Test Case 2
let num2 = 20; // "020"

if (num2 > 10 && num2 < 100) {
	console.log(parseInt(`0${num2}`));
}

// Test Case 3
let num3 = 110; // "110"
if (num3 > 100) {
	console.log(num3);
}

let num4 = 9;
let str = "9";
let str2 = "20";

// Output
// ("{num1} Is The Same Value As {str}");

if (num4 == str) {
	console.log(`${num4} Is The Same Value As ${str}`);
}
if (num4 !== str) {
	console.log(`${num4} Is The Same Value As ${str} And The Same Type`);
}
if (num4 !== str2) {
	console.log(`${num4} Is Not The Same Value Or The Same Type As ${str2}`);
}
if (typeof str === typeof str2 && str !== str2) {
	console.log(`${str} Is The Same Type As ${str2} But Not The Same Value`);
}

let num5 = 10;
let num6 = 30;
let num7 = "30";

if (
	num7 > num5 &&
	typeof num7 !== typeof num5 &&
	num7 > num5 &&
	num7 == num6 &&
	typeof num7 !== typeof num6 &&
	num7 !== num5 &&
	typeof num7 !== typeof num5 &&
	typeof num7 !== typeof num6
) {
	console.log(
		"30 Is Larger Than 10 And Type string Not The Same Type As number"
	);
	console.log(
		"30 Is Larger Than 10 And Value Is The Same As 30 And Type string Not The Same Type As number"
	);
	console.log(
		`${num7} Value And Type Is Not The Same As ${num5} And Type Is Not The Same As ${num6}`
	);
}

// Needed Output
("30 Is Larger Than 10 And Type string Not The Same Type As number");
("30 Is Larger Than 10 And Value Is The Same As 30 And Type string Not The Same Type As number");
("{num3} Value And Type Is Not The Same As {num1} And Type Is Not The Same As {num2}");


// Edit What You Want Here

let num8 = 11;
let num9 = 8;
let num10 = +"11";
let num11 = 35;

/*
  Do Not Edit Below This Line
  Needed Output
  True 7 Times
*/

// Condition 1

if (num8 > num9) {
  console.log("True");
} else {
  console.log("False");
}

// Condition 2

if (num8 > num9 && num8 < num11) {
  console.log("True");
} else {
  console.log("False");
}

// Condition 3

if (num8 > num9 && num8 === num10) {
  console.log("True");
} else {
  console.log("False");
}

// Condition 4

if ((num8 + num9) < num11) {
  console.log("True");
} else {
  console.log("False");
}

// Condition 5

if ((num8 + num10) < num11) {
  console.log("True");
} else {
  console.log("False");
}

// Condition 6

if ((num8 + num9 + num10) < num11) {
  console.log("True");
} else {
  console.log("False");
}

// Condition 7
if (num11 - (num8 + num10) + num9 === 21) {
  console.log("True");
} else {
  console.log("False");
}