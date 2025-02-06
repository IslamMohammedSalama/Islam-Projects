function sayHello(theName, theGender) {
	theGender === "Male"
		? console.log(`Hello Mr ${theName}`)
		: theGender === "Female"
		? console.log(`Hello Miss ${theName}`)
		: console.log(`Hello ${theName}`);
}

// Needed Output
sayHello("Osama", "Male"); // "Hello Mr Osama"
sayHello("Eman", "Female"); // "Hello Miss Eman"
sayHello("Sameh"); // "Hello Sameh"

console.log("-".repeat(50));

function calculate(firstNum, secondNum, operation = "add") {
	// Your Code Here
	if (secondNum === undefined) {
		console.log(`Second Number Not Found`);
		return;
	}
	if (operation === "add") {
		console.log(firstNum + secondNum);
	} else if (operation === "subtract") {
		console.log(firstNum - secondNum);
	} else if (operation === "multiply") {
		console.log(firstNum * secondNum);
	} else if (operation === "division") {
		console.log(firstNum / secondNum);
	} else {
		console.log("Your Operator Is Not Found");
	}
}

// Needed Output
calculate(20); // Second Number Not Found
calculate(20, 30); // 50
calculate(20, 30, "add"); // 50
calculate(20, 30, "subtract"); // -10
calculate(20, 30, "multiply"); // 600
calculate(30, 2, "division"); // 600
calculate(30, 2, "fff"); // 600

console.log("-".repeat(50));

function ageInTime(theAge) {
	// Your Code Here
	if (theAge > 100 || theAge < 10) {
		console.log("The Age Is Out Of The Range");
	} else {
		console.log(`Age In Years Is ${theAge}`);
		console.log(`Age In Months Is ${theAge * 12}`);
		console.log(`Age In Days Is ${theAge * 12 * 31}`);
		console.log(`Age In Hours Is ${theAge * 12 * 31 * 24}`);
		console.log(`Age In Minutes Is ${theAge * 12 * 31 * 24 * 60}`);
		console.log(`Age In Secounds Is ${theAge * 12 * 31 * 24 * 60 * 60}`);
	}
}

// Needed Output
ageInTime(110); // Age Out Of Range
ageInTime(38); // Months Example => 456 Months

console.log("-".repeat(50));

function checkStatus(a, b, c) {
	// Your Code Here
	let args = [a, b, c];
	let name;
	let age;
	let status;
	for (let index = 0; index < args.length; index++) {
		for (let index = 0; index < args.length; index++) {
			typeof args[index] === "string"
				? (name = args[index])
				: typeof args[index] === "number"
				? (age = args[index])
				: typeof args[index] === "boolean"
				? (status = args[index])
				: console.log();
		}
	}
	console.log(
		`Hello ${name}, Your Age Is ${age}, ${
			status === true
				? "You Are Available For Hire"
				: "You Are Not Available For Hire"
		}`
	);
}

// Needed Output
checkStatus("Osama", 38, true); // "Hello Osama, Your Age Is 38, You Are Available For Hire"
checkStatus(38, "Osama", true); // "Hello Osama, Your Age Is 38, You Are Available For Hire"
checkStatus(true, 38, "Osama"); // "Hello Osama, Your Age Is 38, You Are Available For Hire"
checkStatus(false, "Osama", 38); // "Hello Osama, Your Age Is 38, You Are Not Available For Hire"

console.log("-".repeat(50));

function createSelectBox(startYear, endYear) {
	document.write("<select>");
	for (let index = startYear; index <= endYear; index++) {
		document.write(`<option value="${index}">${index}</option>`);
	}
	document.write("</select>");
}
createSelectBox(2000, 2021);

console.log("-".repeat(50));

function multiply(...nums) {
	let result = 1;
	for (let index = 0; index < nums.length; index++) {
		if (typeof nums[index] !== "number") {
			continue;
		} else {
			result = result * parseInt(nums[index]);
		}
	}
	console.log(result);
}

multiply(10, 20); // 200
multiply("A", 10, 30); // 300
multiply(100.5, 10, "B"); // 1000
