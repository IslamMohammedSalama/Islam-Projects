let myFriends = ["Ahmed", "Elham", "Osama", "Gamal"];
let num = 3;

// Method 1
console.log(myFriends.slice(num - num, num)); // ["Ahmed", "Elham", "Osama"];

// Method 2
myFriends.pop();
console.log(myFriends); // ["Ahmed", "Elham", "Osama"];

let friends = ["Ahmed", "Eman", "Osama", "Gamal"];

friends.shift();
friends.pop();

console.log(friends); // ["Eman", "Osama"]

let arrOne = ["C", "D", "X"];
let arrTwo = ["A", "B", "Z"];
let finalArr = [];

finalArr = finalArr.concat(arrTwo, arrOne, arrTwo.pop()).reverse();
console.log(finalArr); // ["Z", "X", "D", "C", "B", "A"]

let website = "Go";
let words = [`${website}ogle`, "Facebook", ["Elzero", "Web", "School"]];

console.log(
	words[website.length][website.length - website.length]
		.slice(website.length)
		.toUpperCase()
); // ZERO

let needle = "JS";
let haystack = ["PHP", "JS", "Python"];

// Write 3 Solutions

if (haystack.includes(needle)) {
	console.log("Found");
}
if (needle === haystack[1]) {
	console.log("Found");
}
if (haystack.indexOf(needle)) {
	console.log("Found");
}

let arr1 = ["A", "C", "X"];
let arr2 = ["D", "E", "F", "Y"];
let allArrs = [];

// Your Code Here
allArrs = allArrs
	.concat(
		arr2[arr1.length - (arr2.length - arr1.length)],
		arr1[arr1.length - (arr2.length - arr1.length)],
		arr2[arr2.length - (arr2.length - arr1.length)]
	)
	.join("").toLowerCase();
allArrs = arr1.concat(arr2).sort().slice(arr2.length).join("").toLowerCase();


console.log(allArrs); // fxy
