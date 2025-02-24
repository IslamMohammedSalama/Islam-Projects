// assign One
console.log("-".repeat(40));

let fileName = "Elzero.php";

console.log(fileName.slice(0, fileName.indexOf(".")));
console.log(fileName.slice(fileName.indexOf(".") + 1));

// Elzero
// php

// assign Two
console.log("-".repeat(40));

function addEl(str) {
	if (str === "" || str.startsWith("El")) {
		return str;
	} else {
		return "El" + str;
	}
}

console.log(addEl("")); // ""
console.log(addEl("Elzero")); // Elzero
console.log(addEl("zero")); // Elzero

// assign Three
console.log("-".repeat(40));

let myString = "Hello Elzero Web School @ We Love Programming@ @#!@#$%%^&*";

console.log(
	myString.slice(0, myString.indexOf("@", myString.indexOf("@") + 1))
);
// Output Needed
("Hello Elzero Web School @ We Love Programming");

// assign Four
console.log("-".repeat(40));

function checkRange(n1, n2, n3, n4, n5) {
	if (n1 >= n4 && n1 <= n5 && n2 >= n4 && n2 <= n5 && n3 >= n4 && n3 <= n5)
		return `Yes All Numbers In Range`;
	else return `Not All Numbers Is In Range`;
}

console.log(checkRange(5, 10, 15, 5, 50)); // Yes All Numbers In Range
console.log(checkRange(8, 4, 20, 2, 50)); // Yes All Numbers In Range
console.log(checkRange(10, 15, 20, 5, 18)); // Not All Numbers Is In Range

// assign Five
console.log("-".repeat(40));

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
console.log("-".repeat(40));

function checkBiggestNum(word) {
	return word.split("").sort().pop();
}

console.log(checkBiggestNum("1500654")); // 6
console.log(checkBiggestNum("8509507")); // 9

// assign Seven
console.log("-".repeat(40));

let nums = [20, 100, 50, 10, 15, -20, 30];

console.log([Math.max(...nums), Math.max(...[nums.sort().pop()])]);

// Needed Output
// [100, 50]

// assign Eight
console.log("-".repeat(40));

let numsTwo = [10, 80, 85, 25, 30, 88, 15];
let goal = 100;

// Your Code Here

console.log(`Closest Number Is ${numsTwo.sort().pop()}`);

// Closest Number Is 88

// assign Nine
console.log("-".repeat(40));

function swapEveryTwoChars(word) {
	// Your Code Here
	let finalWord = "";
	for (let l in word.split("")) {
		if (parseInt(l) === 0) {
			finalWord = finalWord + word[l].toUpperCase();
			continue;
		} else if (word[l] === word[l].toUpperCase()) {
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
console.log("-".repeat(40));

String.prototype.elzeroRepeat = function (val) {
	let final = "";
	for (let index = 0; index < val; index++) {
		final = final + this;
	}
	return final;
};

console.log("Elzero ".elzeroRepeat(3)); // Elzero Elzero Elzero

// assign Eleven
console.log("-".repeat(40));

let myMoney = 5301503206;

console.log(
	myMoney
		.toString()
		.match(/\d{1,3}/g)
		.join(",")
);
// console.log(myMoney.toLocaleString())

// Needed Output
// 5,301,503,206

// assign Twilve
console.log("-".repeat(40));

let names = ["Osso", "Aola", "Essa", "Igaa", "Daad", "Roor"];
let result = [];

for (let index = 0; index < names.length; index++) {
	let fristL = names[index][0];
	let lastL = names[index].slice(-1);
	if (fristL.toLowerCase() === lastL) {
		result.push(names[index]);
	}
}

console.log(result); // ['Osso', 'Aola', 'Daad', 'Roor']

// assign Thirdteen
console.log("-".repeat(40));

let theName = "Elzero";

console.log(`Line 1 => ${theName[0] + theName.slice(-1)}
Line 2 => ${theName.slice(1, -1)}
Line 3 => ${theName.slice(2, -2)}`);

// Line 1 => Eo
// Line 2 => lzer
// Line 3 => ze

// assign FourTeen
console.log("-".repeat(40));

function repeatWithRules(word) {
	let result = "";
	let repeat = 1;
	for (let index = 0; index < word.length; index++) {
		if (index === 0) {
			result = result + word[index];
			repeat++;
		} else {
			result = result + word[index].repeat(repeat);
			repeat++;
		}
	}
	return result;
}

console.log(repeatWithRules("Elzero")); // Ellzzzeeeerrrrroooooo
console.log(repeatWithRules("Hello")); // Heelllllllooooo

// assign FivTeen
console.log("-".repeat(40));

function concatenateWithoutLast(words) {
	for (let index = 0; index < words.length; index++) {
		words[index] = words[index].slice(0, -1);
	}
	return words.join(" ");
}

console.log(concatenateWithoutLast(["Elzeros", "Webd", "Schoold"])); // Elzero Web School

// assign SixTeen
console.log("-".repeat(40));

function getCharacters(word, nums) {
	let fristLetters = word.slice(0, nums);
	let LastLetters = word.slice(-nums);
	return fristLetters + LastLetters;
}

console.log(getCharacters("Elzero School", 2)); // Elol
console.log(getCharacters("Elzero School", 3)); // Elzool

// assign SevenTeen
console.log("-".repeat(40));

function formatName(theName) {
	let numToMakeIt = theName.split(" ").length;
	let result = "";
	console.log(theName);
	for (let index = 0; index < numToMakeIt; index++) {
		let fristL = theName.split(" ")[index][0];
		if (index === 0) {
			result = result + fristL + ".";
		} else {
			result = result + fristL.toLowerCase() + ".";
		}
	}
	return result;
}

console.log(formatName("Osama Elzero")); // O.e
console.log(formatName("Elzero Web School")); // E.w.s

// assign EightTeen
console.log("-".repeat(40));

let st = "elzero";

console.log(st.charAt(0).toUpperCase() + st.slice(1));
console.log(st[0].toUpperCase() + st.slice(1));
console.log(st.substring(0, 1).toUpperCase() + st.slice(1));
console.log(`${st.split("")[0].toUpperCase()}${st.slice(1)}`);
console.log(`${st.substr(0, 1).toUpperCase()}${st.slice(1)}`);
console.log(Array.from(st)[0].toUpperCase() + st.slice(1));
console.log(
	Array.from(st, (e, index) => (index === 0 ? e.toUpperCase() : e)).join("")
);

// Output Needed
// ("Elzero");
// ("Elzero");
// ("Elzero");
// ("Elzero");
// ("Elzero");
// ("Elzero");
// ("Elzero");

// assign NinetTeen
console.log("-".repeat(40));

let stTwo = "Web SchoolElzero ";

stTwo = stTwo.slice(-7) + stTwo.slice(-18, -7);

console.log(stTwo);

// Needed Output
// "Elzero Web School"

// assign Twinty
console.log("-".repeat(40));

let stThree = "Elzero";
console.log(stThree.slice(-1));
console.log(Array.from(stThree)[5]);
console.log(stThree.substr(-1, 1));
console.log(stThree.substring(5));
console.log(stThree[5]);
console.log(stThree.charAt(5));
console.log([...stThree][5]);

// Needed Output
// ("o");
// ("o");
// ("o");
// ("o");
// ("o");
// ("o");
// ("o");

// assign TwintyOne
console.log("-".repeat(40));

function getLastDigit(num) {
	return parseInt(num.toString().slice(-1));
}

console.log(getLastDigit(1)); // 1
console.log(getLastDigit(18)); // 8
console.log(getLastDigit(305)); // 5
console.log(getLastDigit(1569)); // 9
console.log(typeof getLastDigit(1569)); // Number

// assign TwintyTwo
console.log("-".repeat(40));

let str1 = "AElzero";
let str2 = "ZAcademy";

console.log(str1.slice(1) + "\u0020" + str2.slice(1)); // Elzero Academy

// assign TwintyThree
console.log("-".repeat(40));

function reversing(str) {
	let strToArr = str.split("");
	[strToArr[2], strToArr[6]] = [strToArr[6], strToArr[2]];
	[strToArr[11], strToArr[15]] = [strToArr[15], strToArr[11]];
	return strToArr.join("");
}

console.log(reversing(",@Hello, E@lzero")); // ,@olleH, E@orezl

// assign TwintyFour
console.log("-".repeat(40));

function dashBetweenOdd(num) {
	let numtoArr = [...`${num}`];
	let result = "";
	for (let index = 0; index < `${num}`.length; index++) {
		result += numtoArr[index];
		if (
			parseInt(numtoArr[index]) % 2 !== 0 &&
			parseInt(numtoArr[index + 1]) % 2 !== 0 &&
			!isNaN(numtoArr[index + 1])
		) {
			result += "-";
		}
	}
	return result;
}

console.log(dashBetweenOdd(150653127)); // 1-5065-3-127
console.log(dashBetweenOdd(5314557922)); // 5-3-145-5-7-922


// assign TwintyFive
console.log("-".repeat(40));

let myArr = [10, 10, 20, 20, 10, 30, 50, 20, 10];

myArr.length = 0;
console.log(myArr)

myArr = []
console.log(myArr)
let len = myArr.length
for (let index = 0; index < len; index++) {
	myArr.shift()
}
console.log(myArr)
myArr.splice(0,myArr.length)
console.log(myArr)

// Output Needed
// []

