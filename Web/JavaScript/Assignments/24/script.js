let DateNow = new Date();

let mybd = new Date("Sep 18 , 2011");

let diff = DateNow - mybd;

console.log(DateNow);
console.log(mybd);
console.log(`${(diff / 1000).toFixed(0)} Secounds`);
console.log(`${(diff / 1000 / 60).toFixed(0)} Minutes`);
console.log(`${(diff / 1000 / 60 / 60).toFixed(0)} Hours`);
console.log(`${(diff / 1000 / 60 / 60 / 24).toFixed(0)} Days`);
console.log(`${(diff / 1000 / 60 / 60 / 24 / 31).toFixed(0)} Months`);
console.log(`${(diff / 1000 / 60 / 60 / 24 / 31 / 12).toFixed(0)} Years`);
console.log(`${(diff / 1000 / 60 / 60 / 24 / 31 / 12 / 10).toFixed(1)} Knots`);

let newDate = new Date(0);
newDate.setHours(0);
newDate.setFullYear(newDate.getFullYear() + 10);
newDate.setSeconds(newDate.getSeconds() + 1);

console.log(newDate);

// -------
let newDateTwo = new Date();

newDateTwo.setDate(0);

console.log(newDateTwo);
let mL = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December",
];

console.log(
	`Previous Month Is ${
		mL[newDateTwo.getMonth()]
	} And Last Day Is ${newDateTwo.getDate()}`
);

console.log(new Date("sep 18 , 2011"));
console.log(new Date(2011, 8, 18));
console.log(new Date("9 18 2011"));

// let before = performance.now();

// for (let index = 0; index <= 99999; index++) {
// 	console.log(index);
// }

// let after = performance.now();

// console.log(
// 	`Before => ${before.toFixed(0)} , After => ${after.toFixed(
// 		0
// 	)} , Before - After : ${(after - before).toFixed(0)}`
// );

// console.log(`Loop Took ${(after - before).toFixed(0)} Milliseconds.`);

// Write Your Generator Function Here

function* gen() {
	let index = 14;
	yield index;
	let num = 140;
	let sum = index + num;
	while (true) {
		yield sum;
		sum += num += 200;
	}
}

let generator = gen();

console.log(generator.next()); // {value: 14, done: false}
console.log(generator.next()); // {value: 154, done: false}
console.log(generator.next()); // {value: 494, done: false}
console.log(generator.next()); // {value: 1034, done: false}
console.log(generator.next()); // {value: 1774, done: false}
console.log(generator.next()); // {value: 2714, done: false}
console.log(generator.next()); // {value: 3854, done: false}
console.log(generator.next()); // {value: 5194, done: false}
console.log(generator.next()); // {value: 6734, done: false}

function* genNumbers() {
	yield* [1, 2, 2, 2, 3, 4, 5];
}
function* genLetters() {
	yield* ["A", "B", "B", "B", "C", "D"];
}

// Write Your Generator Function Here
function* genAll() {
	yield* new Set(genNumbers());
	yield* new Set(genLetters());
}

let generatorTwo = genAll();

console.log(generatorTwo.next()); // {value: 1, done: false}
console.log(generatorTwo.next()); // {value: 2, done: false}
console.log(generatorTwo.next()); // {value: 3, done: false}
console.log(generatorTwo.next()); // {value: 4, done: false}
console.log(generatorTwo.next()); // {value: 5, done: false}
console.log(generatorTwo.next()); // {value: "A", done: false}
console.log(generatorTwo.next()); // {value: "B", done: false}
console.log(generatorTwo.next()); // {value: "C", done: false}
console.log(generatorTwo.next()); // {value: "D", done: false}

// // main.js File
import calc , * as modOne from "./mod-two.js";
console.log(calc(modOne.numOne, modOne.numTwo, modOne.numThree)); // 60
