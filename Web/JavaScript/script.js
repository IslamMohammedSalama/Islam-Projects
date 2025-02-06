/* 
// Variable And Concatenation Challenge
let title = "Elzero";

let desc = "Elzero Web School";
let date = "25/4";

let card = `
<div class="card" >
<h3 class="title">${title}</h3>
<p class="desc">${desc}</p>
<span class="date">${date}</span>
</div>
`;
document.write(card.repeat(4));
*/

/* 
// Challenge 1


let a = 10;
let b = "20";
let c = 80;

console.log(++a + +b++ + +c++ - +a++); // 10 + 21 + 81 - 12 = 100 
console.log(++a + -b + +c++ - -a++ + +a); // 13 - 21 + 82  + 13 + 13 = 100
console.log(--c + +b + --a * +b++ - +b * a + --a - +true); // 81 + 21 + 13 * 21 - 22 * 13 + 12 - 1 = 100


  [++a] [+]
  [++a]
  - Value:
  - Explain:
  [+]
  - Explain:



//   Challenge 2


let d = "-100";
let e = "20";
let f = 30;
let g = true;

// Only Use Variables Value
// Do Not Use Variable Twice


console.log(-d * e); // 2000
console.log(-d + ++f + (++e * ++g) ); // 173
*/

/* 

let a = 1_00;
let b = 2_00.5;
let c = 1e2;
let d = 2.4;
// Find The Smallest Number On Intager
console.log(Math.round(Math.min(a, b, c, d)));

// Use a and d to get 10000
console.log(Math.pow(a, Math.round(d)));

// Get Int 2 With Four Ways With d
console.log(Math.round(d));
console.log(Math.floor(d));
console.log(parseInt(d));
console.log(Math.trunc(d));

// Use Vars b + d to get This Values

console.log((Math.floor(b) / Math.ceil(d)).toFixed(2)); // 66.67 => string
console.log(Math.round(b) / Math.ceil(d)); // 67 => number
 */

/*
  String Challenge
  All Solutions Must Be In One Chain
  You Can Use Concatenate
*/
/* 
let a = "Elzero Web School";

// Include This Method In Your Solution [slice, charAt]
console.log(`${a.charAt(2).toUpperCase()}${a.slice(3, 6)}`); // Zero

// 8 H
console.log(a.substr(-4, 1).toUpperCase().repeat(8)); // HHHHHHHH

// Return Array
console.log(a.split(" ", 1)); // ["Elzero"]

// Use Only "substr" Method + Template Literals In Your Solution
console.log(a.substr(0, 10)); // Elzero School

// Solution Must Be Dynamic Because String May Changes
console.log(
	`${a.charAt(0).toLowerCase()}${a.slice(1, -1).toUpperCase()}${a
		.substr(-1, 1)
		.toLowerCase()}`
); // eLZERO WEB SCHOOl
 */

/*
  If Condition Challenge
*/

/* let a = 10;

if (a < 10) {
	console.log(10);
} else if (a >= 10 && a <= 40) {
	console.log("10 To 40");
} else if (a > 40) {
	console.log("> 40");
} else {
	console.log("Unknown");
}

a < 10
	? console.log(10)
	: a >= 10 && a <= 40
	? console.log("10 To 40")
	: a > 40
	? console.log("> 40")
	: console.log("Unknown");

// Write Previous Condition With Ternary If Syntax

let st = "Elzero Web School";

if ((st.length * 2).toString() === "34") {
	console.log("Good 1");
}

// W Position May Change
if (st.charAt(st.toLowerCase().indexOf("w", 0)).toLowerCase() === "w") {
	console.log("Good 2");
}
if (!typeof st.toString() !== "string") {
	console.log("Good 3");
}

if (typeof st.length === "number") {
	console.log("Good 4");
}

if (st.slice(0, 6).repeat(2) === "ElzeroElzero") {
	console.log("Good 5");
}
 */

/*
  Switch Challenge
*/

// let job = "Manager";
// let salary = 0;

// if (job === "Manager") {
//   salary = 8000;
// } else if (job === "IT" || job === "Support") {
//   salary = 6000;
// } else if (job === "Developer" || job === "Designer") {
//   salary = 7000;
// } else {
//   salary = 4000;
// }

// switch (job) {
// 	case "Manager":
// 		salary = 8000;
// 		break;
// 	case "IT":
// 	case "Support":
// 		salary = 6000;
//     break;
// 	case "Developer":
// 	case "Designer":
// 		salary = 7000;
//     break;
// 	default:
// 		salary = 4000;
//     break;
// }
// console.log(`My Salary Is ${salary}`);
/*
  If Challenge
*/

// let holidays = 0;
// let money = 0;

// switch (holidays) {
// 	case 0:
// 		money = 5000;
// 		console.log(`My Money is ${money}`);
// 		break;
// 	case 1:
// 	case 2:
// 		money = 3000;
// 		console.log(`My Money is ${money}`);
// 		break;
// 	case 3:
// 		money = 2000;
// 		console.log(`My Money is ${money}`);
// 		break;
// 	case 4:
// 		money = 1000;
// 		console.log(`My Money is ${money}`);
// 		break;
// 	case 5:
// 		money = 0;
// 		console.log(`My Money is ${money}`);
// 		break;
// 	default:
// 		money = 0;
// 		console.log(`My Money is ${money}`);
// }

// if (holidays === 0) {
// 	money = 5000;
// 	console.log(`My Money is ${money}`);
// } else if ((holidays === 1) | (holidays === 2)) {
// 	money = 3000;
// 	console.log(`My Money is ${money}`);
// } else if (holidays === 3) {
// 	money = 2000;
// 	console.log(`My Money is ${money}`);
// } else if (holidays === 4) {
// 	money = 1000;
// 	console.log(`My Money is ${money}`);
// } else if (holidays === 5) {
// 	money = 0;
// 	console.log(`My Money is ${money}`);
// } else {
// 	money = 0;
// 	console.log(`My Money is ${money}`);
// }

/*
  Array Challenge
*/

/* let zero = 0;

let counter = 3;

let my = ["Ahmed", "Mazero", "Elham", "Osama", "Gamal", "Ameer"];

// Write Code Here

my = my.slice(zero, ++counter).reverse();

console.log(my); // ["Osama", "Elham", "Mazero", "Ahmed"];
my = my.slice(++zero, --counter);
console.log(my); // ["Elham", "Mazero"]

console.log(`${my[0].substr(0, 2)}${my[1].substr(2, 4)}`); // "Elzero"

console.log(`${my[1][4].toLowerCase()}${my[1][5].toUpperCase()}`); // "rO"
 */
/* 
  Loop Challenge
*/

/* let myAdmins = ["Ahmed", "Osama", "Sayed", "Stop", "Samera"];
let myEmployees = [
	"Amgad",
	"Samah",
	"Ameer",
	"Omar",
	"Othman",
	"Amany",
	"Samia",
	"Anwar",
];

document.write(`<div>We Have ${myAdmins.length} Admins</div>`);

for (let index = 0; index < myAdmins.length; index++) {
	let counter = index + 1;
	if (myAdmins[index] === "Stop") {
		break;
	}
	document.write("<hr>");
	document.write(
		`<div>The Admin For Team ${counter} Is ${myAdmins[index]}</div>`
	);
	document.write("<h2>Team Members : </h2>");
	let counter2 = 0;
	for (let index2 = 0; index2 < myEmployees.length; index2++) {
		if (myAdmins[index].charAt(0) == myEmployees[index2].charAt(0)) {
			counter2++;
			document.write(`<div>${counter2} - ${myEmployees[index2]}</div>`);
		}
	}
}
 */

/*
  Function - Random Argument Challenge
  ====================================
  Create Function showDetails
  Function Accept 3 Parameters [a, b, c]
  Data Types For Info Is
  - String => Name
  - Number => Age
  - Boolean => Status
  Argument Is Random
  Data Is Not Sorted Output Depend On Data Types
  - Use Ternary Conditional Operator
*/

function showDetails(...args) {
	let name = "UnKnown";
	let age = "UnKnown";
	let status = "UnKnown";
	for (let index = 0; index < args.length; index++) {
		typeof args[index] === "string"
			? (name = args[index])
			: typeof args[index] === "number"
			? (age = args[index])
			: typeof args[index] === "boolean"
			? (status = args[index])
			: console.log();
	}
	console.log(
		`Hello ${name}, Your Age Is ${age}, ${
			status === true
				? "You Are Available For Hire"
				: "You Are Not Available For Hire"
		}`
	);
}

showDetails("Osama", 38, true); // "Hello Osama, Your Age Is 38, You Are Available For Hire"
showDetails(38, "Osama", true); // "Hello Osama, Your Age Is 38, You Are Available For Hire"
showDetails(true, 38, "Osama"); // "Hello Osama, Your Age Is 38, You Are Available For Hire"
showDetails(false, "Osama", 38); // "Hello Osama, Your Age Is 38, You Are Not Available For Hire"
