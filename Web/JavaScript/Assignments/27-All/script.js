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
console.log(myArr);

myArr = [];
console.log(myArr);
let len = myArr.length;
for (let index = 0; index < len; index++) {
	myArr.shift();
}
console.log(myArr);
myArr.splice(0, myArr.length);
console.log(myArr);

// Output Needed
// []

// assign TwintySix
console.log("-".repeat(40));

let myArrTwo = [10, 10, 20, 20, 10, 30, 50, 20, 10];

console.log(Array.from(new Set(myArrTwo)));

let newArr = [];

for (let index = 0; index < myArrTwo.length; index++) {
	let preItem = 0;
	if (index === 0) {
		newArr.push(myArrTwo.sort()[index]);
	} else {
		preItem = myArrTwo.sort()[index - 1];
		if (preItem !== myArrTwo.sort()[index]) {
			newArr.push(myArrTwo.sort()[index]);
		} else {
			continue;
		}
	}
}
console.log(newArr);

console.log(
	myArrTwo.sort().reduce((acc, curr) => {
		return acc.includes(curr) ? acc : [...acc, curr];
	}, [])
);

console.log(myArrTwo.sort().filter((v, i) => myArrTwo.indexOf(v) === i));

// Output Needed
// [10, 20, 30, 50]

// assign TwintySeven
console.log("-".repeat(40));

let myArrThree = ["69", "108", "122", "101", "114", "111"];

// Your Code Here

let nArr = myArrThree.map((val) => String.fromCharCode(val)).join("");

console.log(nArr);

// assign TwintyEight
console.log("-".repeat(40));

// Write Your Function Here
function customMerge(...arreys) {
	let result = [];
	for (let index = 0; index < arreys.length; index++) {
		result = result.concat([...arreys[index]]);
	}
	for (let index = 0; index < result.length; index++) {
		result[index] = parseInt(result[index]);
	}
	return result.sort();
}

console.log(
	customMerge([10, 20, "30", 1000], [100, "50", 20], [90, 20, "40", 10])
);
// [10, 10, 20, 20, 20, 30, 40, 50, 90, 100, 1000]

// assign TwintyNine
console.log("-".repeat(40));

// Write Your Function Here

function customCalc(...args) {
	let numsOnly = [];
	let result = 0;
	for (let index = 0; index < args.length; index++) {
		if (typeof +args[index] === "number" && !isNaN(+args[index])) {
			numsOnly.push(+args[index]);
		}
	}
	console.log(numsOnly);
	for (let index = 0; index < numsOnly.length; index++) {
		result += numsOnly[index];
	}
	return result * numsOnly[0] * numsOnly[numsOnly.length - 1];
}

console.log(customCalc("10", 20, "A", "40", 15));
// 12750 <= (10 + 20 + 40 + 15) * 10 * 15

console.log(customCalc(5, "15", 10, 5, 10));
// 2250 <= (5 + 15 + 10 + 5 + 10) * 5 * 10

console.log(customCalc(30, 5, "C", 10));
// 13500 <= (30 + 5 + 10) * 30 * 10

// assign Thirty
console.log("-".repeat(40));

for (let i = 1; i < 100; i += 5) {
	console.log(i);
	i += 5;
}

// Output Needed
// 1;
// 11;
// 21;
// 31;
// 41;
// 51;
// 61;
// 71;
// 81;
// 91;

// assign ThirtyOne
console.log("-".repeat(40));

let myArray = [100, 200, 300, 400];

// Method 1

let clonedArray = [...myArray];
console.log(clonedArray); // [100, 200, 300, 400]

// Method 2
clonedArray = [];

clonedArray = myArray;
console.log(clonedArray); // [100, 200, 300, 400]

// Method 3
clonedArray = [];

clonedArray = Array.from(myArray);
console.log(clonedArray); // [100, 200, 300, 400]

// Method 4
clonedArray = [];

clonedArray = Object.assign([], myArray);
console.log(clonedArray); // [100, 200, 300, 400]

// Method 5

clonedArray = [];
for (let index = 0; index < myArray.length; index++) {
	clonedArray.push(myArray[index]);
}

console.log(clonedArray); // [100, 200, 300, 400]

// Method 6
clonedArray = [];

clonedArray.push(...myArray);
console.log(clonedArray); // [100, 200, 300, 400]

// Method 7
clonedArray = [];

clonedArray.unshift(...myArray);
console.log(clonedArray); // [100, 200, 300, 400]

// Method 7

clonedArray = myArray.map((e) => e);
console.log(clonedArray); // [100, 200, 300, 400]

// Method 8

clonedArray = [].concat(myArray);
console.log(clonedArray); // [100, 200, 300, 400]

// Method 9

clonedArray = myArray.filter((e) => e);

console.log(clonedArray); // [100, 200, 300, 400]

// assign ThirtyTwo
console.log("-".repeat(40));

let strNumber = "10";

// Method 1
console.log(strNumber * 1); // 10
console.log(strNumber - 0); // 10 <= Same Solution

// Method 2
console.log(parseInt(strNumber));

// Method 3
console.log(parseFloat(strNumber));

// Method 4
console.log(+strNumber);

// Method 5
console.log(Number(strNumber));

// Method 6
console.log(strNumber / 1);

// Method 7
console.log(strNumber - 0);

// Output Needed
10;

// assign ThirtyThree
console.log("-".repeat(40));

console.log(
	"%cElzero Web School",
	`
background-color : #0075ff ;
padding:20px;
font-size:30px;
font-weight : bold;
`
);
// assign ThirtyFour
console.log("-".repeat(40));

let arr = [1, 1, 1, 2, 3, 4, 3];

let uniqueElements = Array.from(new Set(arr));
console.log(uniqueElements); // [1, 2, 3, 4]

uniqueElements = arr.reduce(
	(acc, curr) => (acc.includes(curr) ? acc : [...acc, curr]),
	[]
);

console.log(uniqueElements); // [1, 2, 3, 4]
uniqueElements = arr.filter((v, i) => arr.indexOf(v) === i);
console.log(uniqueElements);

uniqueElements = [];
arr.sort();
for (let index = 0; index < arr.length; index++) {
	let preItem = 0;
	if (index === 0) {
		uniqueElements.push(arr[index]);
	} else {
		preItem = arr[index - 1];
		if (preItem !== arr[index]) {
			uniqueElements.push(arr[index]);
		} else {
			continue;
		}
	}
}

console.log(uniqueElements);

// assign ThirtyFive
console.log("-".repeat(40));

let chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
let leng = 20;
let randomSeiral = "";

for (let index = 0; index < leng; index++) {
	randomSeiral += chars[Math.floor(Math.random() * chars.length)];
}

console.log(randomSeiral);

// assign ThirtySix
console.log("-".repeat(40));

let aToZ = "abcdefghijklmnopqrstuvwxyz";
aToZ = "";
for (let index = 65; index < 91; index++) {
	aToZ += String.fromCharCode(index).toLowerCase();
}

console.log(aToZ);

let numOne = 100;
let numTwo = 200;

// assign ThirtySeven
console.log("-".repeat(40));

if (numOne > numTwo) {
	console.log("1st > 2nd");
} else if (numOne < numTwo) {
	console.log("1st < 2nd");
} else {
	console.log("1st = 2nd");
}

// 1st < 2nd

// Write Your Ternary Operator Code Here
console.log(
	numOne > numTwo ? "1st > 2nd" : numOne < numTwo ? "1st < 2nd" : "1st = 2nd"
);

numOne > numTwo
	? console.log("1st > 2nd")
	: numOne < numTwo
	? console.log("1st < 2nd")
	: console.log("1st = 2nd");

// assign ThirtyEight
console.log("-".repeat(40));

let str = "i lovE elzeRO weB schOOL";
let strAfter = "";

for (let index = 0; index < str.split(" ").length; index++) {
	strAfter +=
		str.split(" ")[index].charAt(0).toUpperCase() +
		str.split(" ")[index].slice(1).toLowerCase() +
		" ";
}

console.log(strAfter);

// Output Needed
("I Love Elzero Web School");

// assign ThirtyNine
console.log("-".repeat(40));

let myData = ["Osama", "Mohamed", "Elsayed", "Elzero"];

// Write Your Code Here

Object.defineProperty(myData, "length", { writable: false });

// myData.push();  // Error
console.log(myData); // ['Osama', 'Mohamed', 'Elsayed', 'Elzero']

// assign FourtyOne
console.log("-".repeat(40));

const myDataTwo = {
	user: "Elzero",
	age: 41,
	country: "Egypt",
};

// Write Your Code Here

Object.defineProperty(myDataTwo, "skill", {
	writable: false,
});

// myDataTwo.skill = "Programming"; // Error

console.log(myDataTwo.user); // Elzero
console.log(myDataTwo.age); // 41
console.log(myDataTwo.country); // Egypt
console.log(myDataTwo.skill); // Undefined

// assign FourtyTwo
console.log("-".repeat(40));

document.addEventListener("keydown", function (e) {
	if (e.ctrlKey && e.altKey && e.shiftKey) {
		console.log("You Pressed Ctrl + Alt + Shift");
	}
});

// assign FourtyThree
console.log("-".repeat(40));

let newProm = new Promise((res, rej) => {
	let newReq = new XMLHttpRequest();
	newReq.open("Get", "https://api.github.com/users/ElzeroWebSchool/repos");
	newReq.send();
	newReq.onload = function () {
		if (this.readyState === 4 && this.status === 200) {
			res(this.responseText);
		} else {
			rej(new Error("Not Found"));
		}
	};
});

let table = document.querySelector("tbody");

newProm.then((data) => {
	let ourData = JSON.parse(data);
	console.log(ourData);
	for (let index = 0; index < ourData.length; index++) {
		let newRow = document.createElement("tr");
		let repoName = document.createElement("td");
		repoName.innerText = ourData[index].name;
		let stars = document.createElement("td");
		stars.innerText = ourData[index].stargazers_count;
		let link = document.createElement("td");
		let visitButton = document.createElement("a");
		visitButton.href = ourData[index].html_url;
		visitButton.innerHTML = `Link Here To Visit`;
		visitButton.target = "_blank";
		link.append(visitButton);
		newRow.append(repoName, stars, link);
		table.appendChild(newRow);
	}
});

// assign FourtyFour
console.log("-".repeat(40));

let last = 30;

function* getodd() {
	let nums = [];
	let result = 0;
	let index = 0;
	while (last !== 1) {
		if (index === 0) {
			last -= 1;
			nums.push(last);
			yield last;
		} else {
			last -= 4;
			nums.push(last);
			yield last;
		}
		index++;
	}
	for (let index = 0; index < nums.length; index++) {
		result += nums[index];
	}
	yield result;
}
let gen = getodd();

for (let index = 0; index <= 8; index++) {
	console.log(gen.next().value);
}

// First Request Output Needed
29;
25;
21;
17;
13;
9;
5;
1;

// Second Request Output Needed
120;

// assign FourtyFive
console.log("-".repeat(40));

let rangeEnd = 10;
let myRange = [];

for (let index = 1; index <= rangeEnd; index++) {
	myRange.push(index);
}

console.log(myRange); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myRange = [];

let index = 1;
while (index <= rangeEnd) {
	myRange.push(index);
	index++;
}
console.log(myRange); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

myRange = [];
index = 10;

while (index > 0) {
	myRange.unshift(index);
	index--;
}

// Output Needed
console.log(myRange); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// assign FourtySix
console.log("-".repeat(40));

let numsThree = [10, -20, 300, 50, 100, -50];

let maxNumber = Math.max(...numsThree);
console.log(maxNumber); // 300

maxNumber = 0;
for (let index = 0; index < numsThree.length; index++) {
	if (maxNumber < numsThree[index]) {
		maxNumber = numsThree[index];
	}
}
console.log(maxNumber); // 300

maxNumber = numsThree.reduce((acc, curr) => (acc > curr ? acc : curr));

console.log(maxNumber); // 300

// assign FourtySeven
console.log("-".repeat(40));

let btn = document.querySelector(".form button");

addEventListener("click", (ev) => {
	if (ev.target.tagName === "BUTTON") {
		let link = document.createElement("a");
		let textToSave = document.querySelector(".form textarea").value;
		let newFile = new Blob([textToSave], {
			type: "text/plain",
		});
		link.href = URL.createObjectURL(newFile);
		link.download = "saved-file.txt";
		link.click();
		URL.revokeObjectURL(link.href);
	}
});

// assign FourtyEight
console.log("-".repeat(40));

function createStars(num) {
	let result = "";
	let repeat = 1;
	for (let index = 0; index < num; index++) {
		result = result + "*".repeat(repeat) + "\n";
		repeat += 2;
	}
	return result;
}

console.log(createStars(8));

// Output Needed
//   *
//   ***
//   *****
//   *******
//   *********
//   ***********
//   *************
//   ***************

// assign FourtyNine
console.log("-".repeat(40));

function createStarsTwo(num) {
	let result = "";
	let repeat = 1;
	for (let index = 0; index < num; index++) {
		result = result + "*".repeat(repeat) + "\n";
		repeat += 2;
	}
	for (let index = -1; index < num; index++) {
		console.log("hello");
		result = result + "*".repeat(repeat) + "\n";
		repeat -= 2;
	}
	return result;
}

console.log(createStarsTwo(3));

// Output Needed
//   *
//   ***
//   *****
//   ***
//   *

console.log(createStarsTwo(7));

// Output Needed
//   *
//   ***
//   *****
//   *******
//   *********
//   ***********
//   *************
//   ***********
//   *********
//   *******
//   *****
//   ***
//   *

// assign Fivty
console.log("-".repeat(40));

function createStarsThree(num) {
	let repeat = num * 2 + 1;
	console.log(repeat);
	let repeatSpace = 0;
	let result = "";
	for (let index = -1; index < num; index++) {
		result = result + " ".repeat(repeatSpace) + "*".repeat(repeat) + "\n";
		repeat -= 2;
		repeatSpace += 1;
	}
	for (let index = 0; index < num; index++) {
		repeat += 2;
		repeatSpace -= 1;
		result = result + " ".repeat(repeatSpace) + "*".repeat(repeat) + "\n";
	}
	return result;
}

console.log(createStarsThree(6));

// Output Needed
// ***********
//  *********
//   *******
//    *****
//     ***
//      *
//      *
//     ***
//    *****
//   *******
//  *********
// ***********
