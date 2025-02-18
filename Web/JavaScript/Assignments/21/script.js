let setOfNumbers = new Set([10]);
setOfNumbers.add(20).add(setOfNumbers.size);

console.log(setOfNumbers);
console.log(Array.from(setOfNumbers)[2]);

console.log("-".repeat(40));

let myFriends = ["Osama", "Ahmed", "Sayed", "Sayed", "Mahmoud", "Osama"];

console.log(new Set(myFriends.sort()));

console.log("-".repeat(40));

let myInfo = {
	username: "Osama",
	role: "Admin",
	country: "Egypt",
};

let newMap = new Map(Object.entries(myInfo));

console.log(newMap);
console.log(newMap.size);
console.log(newMap.has("role"));

console.log("-".repeat(40));

let theNumber = 100020003000;

console.log(
	+[...new Set([...[...theNumber.toString()].filter((e) => e !== "0")])].join(
		""
	)
);

let theName = "Elzero";

console.log([...theName]);
console.log(theName.split(""));
console.log(Array.from(theName));
console.log(Array.from(theName, (e) => e));
console.log(Object.assign([], theName));

console.log("-".repeat(40));

let chars = ["A", "B", "C", "D", "E", 10, 15, 6];

chars.sort().copyWithin(0, 3, 6);

console.log(chars);

chars = ["A", "B", "C", 20, "D", "E", 10, 15, 6];
chars.sort().copyWithin(0, 4, 8);

console.log(chars);

chars = ["Z", "Y", "A", "D", "E", 10, 1];
chars.copyWithin(2);

console.log(chars);

console.log("-".repeat(40));

let numsOne = [1, 2, 3];
let numsTwo = [4, 5, 6];

console.log([...numsOne,...numsTwo])
console.log([...new Set([...numsOne, ...numsTwo])])
console.log(numsOne.concat(numsTwo))


console.log("-".repeat(40));

let n1 = [10, 30, 10, 20];
let n2 = [30, 20, 10];

console.log(Math.max(...n2) * [...n1,...n2].length) // 210