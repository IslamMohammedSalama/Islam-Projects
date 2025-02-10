let mix = [1, 2, 3, "E", 4, "l", "z", "e", "r", 5, "o"];

// Elzero

let word = mix
	.map((ele) => (isNaN(ele) ? ele : ""))
	.reduce((acc, current) => acc + current);

console.log(word);

console.log("-".repeat(20));

let myString = "EElllzzzzzzzeroo";

// Elzero

let wordTwo = myString
	.split("")
	.filter((ele, i) => myString.indexOf(ele) == i)
	.reduce((acc, current) => acc + current);
console.log(wordTwo);

console.log("-".repeat(20));

let myArray = ["E", "l", "z", ["e", "r"], "o"];

// Elzero

let wordThree = myArray.reduce((acc, curr) => acc + curr).replaceAll(",", "");

console.log(wordThree);

console.log("-".repeat(20));

let numsAndStrings = [1, 10, -10, -20, 5, "A", 3, "B", "C"];

// [-1, -10, 10, 20, -5, -3]

let newNums = numsAndStrings
	.filter((ele) => !isNaN(parseInt(ele)))
	.map((ele) => -ele);

console.log(newNums);

console.log("-".repeat(20));

let nums = [2, 12, 11, 5, 10, 1, 99];

// 500
let final = nums.reduce((acc, current) => {
    return current % 2 === 0 ? acc * current : acc + current;
}, 1)


console.log(final);
