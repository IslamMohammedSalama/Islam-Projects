let start = 10;
let end = 100;
let exclude = 40;

for (let i = start; i <= end; i += start) {
	if (i == exclude) {
		continue;
	}
	console.log(i);
}

console.log("=".repeat(10));

let start2 = 10;
let end2 = 0;
let stop = 3;

for (j = start2; j >= stop; j--) {
	if (j >= 10) {
		console.log(j);
	} else {
		console.log(`${end2}${j}`);
	}
}

console.log("=".repeat(10));

let start3 = 1;
let end3 = 6;
let breaker = 2;

for (let index = start3; index <= end3; index++) {
	console.log(index);
	for (let index2 = breaker; index2 < end3; index2 += breaker) {
		console.log(`${"-".repeat(2)} ${index2}`);
	}
}

console.log("=".repeat(10));

let index = 10;
let jump = 2;

for (;;) {
	if (index === jump) {
		break;
	}
	console.log(index);
	index -= jump;
}

console.log("=".repeat(10));

let friends = [
	"Ahmed",
	"Sayed",
	"Eman",
	"Mahmoud",
	"Ameer",
	"Osama",
	"Sameh",
	"Islam",
];
let letter = "a";
let number = letter.length;
for (let index = 1; index < friends.length; index++) {
	if (friends[index].startsWith(letter)) {
		continue;
	}
	if (friends[index].includes(letter)) {
		console.log(`${number} => ${friends[index]}`);
		number++;
	}
}

console.log("=".repeat(10));

let start4 = 0;
let swappedName = "elZerO";
let newName = "";
for (let char = start4; char < swappedName.length; char++) {
	if (swappedName[char] == swappedName[char].toLowerCase()) {
		newName = newName + swappedName[char].toUpperCase();
	} else {
		newName = newName + swappedName[char].toLowerCase();
	}
}
console.log(newName);
console.log("=".repeat(10));

let start5 = 0;
let mix = [1, 2, 3, "A", "B", "C", 4];

for (let index = start5; index < mix.length; index++) {
	if ((mix[index] === 1) || (typeof mix[index] !== "number")) {
		continue;
	}
	console.log(mix[index]);
}
