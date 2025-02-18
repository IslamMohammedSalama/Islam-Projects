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

// function showDetails(...args) {
// 	let name = "UnKnown";
// 	let age = "UnKnown";
// 	let status = "UnKnown";
// 	for (let index = 0; index < args.length; index++) {
// 		typeof args[index] === "string"
// 			? (name = args[index])
// 			: typeof args[index] === "number"
// 			? (age = args[index])
// 			: typeof args[index] === "boolean"
// 			? (status = args[index])
// 			: console.log();
// 	}
// 	console.log(
// 		`Hello ${name}, Your Age Is ${age}, ${
// 			status === true
// 				? "You Are Available For Hire"
// 				: "You Are Not Available For Hire"
// 		}`
// 	);
// }

// showDetails("Osama", 38, true); // "Hello Osama, Your Age Is 38, You Are Available For Hire"
// showDetails(38, "Osama", true); // "Hello Osama, Your Age Is 38, You Are Available For Hire"
// showDetails(true, 38, "Osama"); // "Hello Osama, Your Age Is 38, You Are Available For Hire"
// showDetails(false, "Osama", 38); // "Hello Osama, Your Age Is 38, You Are Not Available For Hire"

/*
  Function Arrow Challenges
*/

// [1] One Statement In Function
// [2] Convert To Arrow Function
// [3] Print The Output [Arguments May Change]

// let names = function (...names) {
// 	return `String [${names.join("], [")}] => Done !`;
// };

// let names = (...names) => `String [${names.join("], [")}] => Done !`

// console.log(names("Osama", "Mohamed", "Ali", "Ibrahim"));
// String [Osama], [Mohamed], [Ali], [Ibrahim] => Done !

/* ================================= */

// [1] Replace ??? In Return Statement To Get The Output
// [2] Create The Same Function With Regular Syntax
// [3] Use Array Inside The Arguments To Get The Output

// let myNumbers = [20, 50, 10, 60];

// let calc = (one, two, ...nums) => one + two + nums[+(!Array.isArray(myNumbers))];
// let calc = function (one, two, ...nums) {
// 	return one + two + nums[+!Array.isArray(myNumbers)];
// }

// console.log(calc(10, 20, 50, 10, 60)); // 80

/*
  Higher Order Functions Challenges

  You Can Use
  - ,
  - _
  - Space
  - True => 1 => One Time Only In The Code

  You Cannot Use
  - Numbers
  - Letters

  - You Must Use [Filter + Map + Reduce + Your Knowledge]
  - Order Is Not Important
  - All In One Chain

*/

// let myString = "1,2,3,EE,l,z,e,r,o,_,W,e,b,_,S,c,h,o,o,l,2,0,Z";

// let solution = myString
// 	.split("")
// 	.map((ele) => (ele === "," ? "" : ele))
// 	.filter((ele) => isNaN(parseInt(ele)))
// 	.reduce((acc, current) => acc + current)
// 	.slice(true, -isNaN(myString))
// 	.replaceAll("_", " ");

// console.log(solution); // Elzero Web School

// body
document.body.style.cssText = `
margin:0;
padding:0;
`;

// header
let header = document.createElement("header");
header.className = "header";

header.style.cssText = `
	padding : 20px;
	display:flex;
	justify-content : space-between;
	align-items : center;
	height:7.5vh;
	width:100%;
	box-sizing : border-box;
`;

let logo = document.createElement("a");
logo.innerHTML = "Elzero";
logo.style.cssText = `
	font-size : 30px;
	font-weight : bold;
	color : #24a76f;
`;

let nav = document.createElement("ul");

nav.style.cssText = `
	list-style:none;
	padding:0;
	margin:0;
	display:flex;
	gap:20px;
`;
let navOne = document.createElement("li");
navOne.innerHTML = "Home";
navOne.style.cssText = `
	color : #777;
`;
let navTwo = document.createElement("li");
navTwo.innerHTML = "About";
navTwo.style.cssText = `
	color : #777;
`;
let navThree = document.createElement("li");
navThree.innerHTML = "Service";
navThree.style.cssText = `
	color : #777;
`;
let navFour = document.createElement("li");
navFour.innerHTML = "Contact";
navFour.style.cssText = `
	color : #777;
`;

nav.appendChild(navOne);
nav.appendChild(navTwo);
nav.appendChild(navThree);
nav.appendChild(navFour);
header.appendChild(logo);
header.appendChild(nav);

// content

let content = document.createElement("section");
content.className = "content";
content.style.cssText = `
	background-color : #ececec;
	height:calc(100vh - (7.5vh * 2));
	width:100%;
	box-sizing:border-box;
	padding:20px;
	display:grid;
	grid-template-columns: repeat(auto-fill,minmax(280px,1fr));
	gap:20px
`;

for (let index = 0; index < 15; index++) {
	let num = index + 1;
	let product = document.createElement("div");
	product.style.cssText = `
	background-color:white;
	display:flex;
	justify-content: center;
	align-items:center;
	flex-flow:column;
	box-sizing:border-box;
	padding:20px;
	`;
	let title = document.createElement("h3");
	title.innerHTML = `${num}`;
	title.style.margin = "0 0 20px 0";
	let name = document.createElement("span");
	name.innerHTML = `Product`;
	product.appendChild(title);
	product.appendChild(name);
	content.appendChild(product);
}
// Footer
let footer = document.createElement("footer");
footer.className = "footer";
footer.style.cssText = `
height:7.5vh;
width:100%;
background-color : #24a76f;
padding:20px;
box-sizing:border-box;
display:flex;
justify-content:center;
align-items:center;
`;
let footerText = document.createElement("p");
footerText.textContent = "CopyRight 2025";

footerText.style.cssText = `
font-size:20px;
color:white;
`;

footer.appendChild(footerText);

document.body.before(header);
document.body.before(content);
document.body.before(footer);

let input = document.querySelector(".input");
let submit = document.querySelector(".add");
let tasksDiv = document.querySelector(".tasks");

// Empty Array To Store The Tasks
let arrayOfTasks = [];

if (localStorage.getItem("tasks")) {
	arrayOfTasks = JSON.parse(localStorage.getItem("tasks"));
}

getDataFromLocalStorage();

tasksDiv.addEventListener("click", (e) => {
	if (e.target.classList.contains("del")) {
		deleteTaskWith(e.target.parentElement.getAttribute("data-id"));
		e.target.parentElement.remove();
	}
	if (e.target.classList.contains("task")) {
		// Toggle Completed For The Task
		toggleStatusTaskWith(e.target.getAttribute("data-id"));
		// Toggle Done Class
		e.target.classList.toggle("done");
	}
});

submit.onclick = () => {
	if (input.value !== "") {
		addTasksToArrey(input.value);
		input.value = "";
	}
};

function addTasksToArrey(taskText) {
	const task = {
		id: Date.now(),
		title: taskText,
		complated: false,
	};
	arrayOfTasks.push(task);
	addDataToLocalStorageFrom(arrayOfTasks);
	addElementsToPageFrom(arrayOfTasks);
}

function addElementsToPageFrom(arr) {
	arr.forEach((element) => {
		let newTask = document.createElement("div");
		newTask.className = "task";
		newTask.innerHTML = element.title;
		if (element.completed) {
			newTask.className = "task done";
		}
		newTask.setAttribute("data-id", element.id);
		let span = document.createElement("span");
		span.innerHTML = "Delete";
		span.className = "del";

		newTask.append(span);
		tasksDiv.append(newTask);
	});
}

function addDataToLocalStorageFrom(arr) {
	localStorage.setItem("tasks", JSON.stringify(arr));
}

function getDataFromLocalStorage() {
	let data = window.localStorage.getItem("tasks");
	if (data) {
		let tasks = JSON.parse(data);
		addElementsToPageFrom(tasks);
	}
}

function deleteTaskWith(taskId) {
	arrayOfTasks = arrayOfTasks.filter((task) => task.id != taskId);
	addDataToLocalStorageFrom(arrayOfTasks);
}
function toggleStatusTaskWith(taskId) {
	for (let i = 0; i < arrayOfTasks.length; i++) {
		if (arrayOfTasks[i].id == taskId) {
			arrayOfTasks[i].completed == false
				? (arrayOfTasks[i].completed = true)
				: (arrayOfTasks[i].completed = false);
		}
	}
	addDataToLocalStorageFrom(arrayOfTasks);
}

/*
  Destructuring
  - Challenge
*/

let chosen = 3;

let myFriends = [
	{ title: "Osama", age: 39, available: true, skills: ["HTML", "CSS"] },
	{ title: "Ahmed", age: 25, available: false, skills: ["Python", "Django"] },
	{ title: "Sayed", age: 33, available: true, skills: ["PHP", "Laravel"] },
];

let [osama, ahmed, sayed] = myFriends;

if (chosen === 1) {
	let {
		title: oTitle,
		age: oAge,
		available: oHire,
		skills: [, oSkillTwo],
	} = osama;
	console.log(oTitle);
	console.log(oAge);
	console.log(oHire ? "Avilable" : "Not Avilable");
	console.log(oSkillTwo);
} else if (chosen === 2) {
	let {
		title: aTitle,
		age: aAge,
		available: aHire,
		skills: [, aSkillTwo],
	} = ahmed;
	console.log(aTitle);
	console.log(aAge);
	console.log(aHire ? "Avilable" : "Not Avilable");
	console.log(aSkillTwo);
} else if (chosen === 3) {
	let {
		title: sTitle,
		age: sAge,
		available: sHire,
		skills: [, sSkillTwo],
	} = sayed;
	console.log(sTitle);
	console.log(sAge);
	console.log(sHire ? "Avilable" : "Not Avilable");
	console.log(sSkillTwo);
}

/*
    Map And Set + What You Learn => Challenge
    Requirements
    - You Cant Use Numbers Or True Or False
    - Don't Use Array Indexes
    - You Cant Use Loop
    - You Cant Use Any Higher Order Function
    - Only One Line Solution Inside Console
    - If You Use Length => Then Only Time Only
    Hints
  - You Can Use * Operator Only In Calculation
    - Set
    - Spread Operator
    - Math Object Methods
*/

let n1 = [10, 30, 10, 20];
let n2 = [30, 20, 10];
console.log(Math.max(...n2) * [...n1, ...n2].length); // 210
