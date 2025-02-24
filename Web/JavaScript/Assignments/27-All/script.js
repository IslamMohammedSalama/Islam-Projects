// assign One

let fileName = "Elzero.php";

console.log(fileName.slice(0, fileName.indexOf(".")));
console.log(fileName.slice(fileName.indexOf(".") + 1));

// Elzero
// php

// assign Two

function addEl(str) {
	if (str === "" || str.startsWith("El")) {
		return "";
	} else {
		return "El" + str;
	}
}

console.log(addEl("")); // ""
console.log(addEl("Elzero")); // Elzero
console.log(addEl("zero")); // Elzero

// assign Three

let myString = "Hello Elzero Web School @ We Love Programming@ @#!@#$%%^&*";

console.log(
	myString.slice(0, myString.indexOf("@", myString.indexOf("@") + 1))
);
// Output Needed
("Hello Elzero Web School @ We Love Programming");

// assign Four

function checkRange(n1, n2, n3, n4, n5) {
	if (n1 >= n4 && n1 <= n5 && n2 >= n4 && n2 <= n5 && n3 >= n4 && n3 <= n5)
		return `Yes All Numbers In Range`;
	else return `Not All Numbers Is In Range`;
}

console.log(checkRange(5, 10, 15, 5, 50)); // Yes All Numbers In Range
console.log(checkRange(8, 4, 20, 2, 50)); // Yes All Numbers In Range
console.log(checkRange(10, 15, 20, 5, 18)); // Not All Numbers Is In Range

// assign Five

function replaceFirstWithLast(word) {
	// Your Code Here
	let fristL = word.slice(-1);
	let lastL = word[0];
	// return fristL  + lastL
	return fristL + word.slice(1, -1) + lastL;
}

console.log(replaceFirstWithLast("olzerE")); // Elzero
console.log(replaceFirstWithLast("Hello")); // oelloH

// assign Six

function checkBiggestNum(word) {
	return word.split("").sort().pop();
}

console.log(checkBiggestNum("1500654")); // 6
console.log(checkBiggestNum("8509507")); // 9

// assign Seven

let nums = [20, 100, 50, 10, 15, -20, 30];

console.log([Math.max(...nums), Math.max(...[nums.sort().pop()])]);

// Needed Output
// [100, 50]

// assign Eight

let numsTwo = [10, 80, 85, 25, 30, 88, 15];
let goal = 100;

// Your Code Here

console.log(`Closest Number Is ${numsTwo.sort().pop()}`);

// Closest Number Is 88

// assign Nine

function swapEveryTwoChars(word) {
	// Your Code Here
	let finalWord = "";
	for (let l in word.split("")) {
		if (parseInt(l) === 0) {
			finalWord = finalWord + word[l].toUpperCase();
			continue;
		}
		else if (word[l] === word[l].toUpperCase()) {
			console.log("Captal Letter Is Here");
			finalWord = finalWord + word[l].toLowerCase();
		} else {
			finalWord = finalWord + word[l];
		}
	}
	return finalWord;
}

console.log(swapEveryTwoChars("elZeRo")); // Elzero
console.log(swapEveryTwoChars("heLlO")); // Hello

// assign Ten

// Write Your Function Implementation Here

String.prototype.elzeroRepeat = function (val) {
	let final = "" ;
	for (let index = 0; index < val; index++) {
		final = final + this
	}
	return final ;
}

console.log("Elzero ".elzeroRepeat(3)); // Elzero Elzero Elzero