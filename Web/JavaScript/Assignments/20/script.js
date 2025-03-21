let myNumbers = [1, 2, 3, 4, 5];

// Write Your Destructuring Assignment Here

let [a, , , , e] = myNumbers;

console.log(a * e); // 5

console.log("-".repeat(20));

let mySkills = [
	"HTML",
	"CSS",
	"JavaScript",
	["PHP", "Python", ["Django", "Laravel"]],
];

// Write Your Destructuring Assignment Here
let [a2, b, c, [d, e2, [f, g]]] = mySkills;

console.log(`My Skills: ${a2}, ${b}, ${c}, ${d}, ${e2}, ${f}, ${g}`);

// My Skills: HTML, CSS, JavaScript, PHP, Python, Django, Laravel

console.log("-".repeat(20));

let arr1 = ["Ahmed", "Sameh", "Sayed"];
let arr2 = ["Mohamed", "Gamal", "Amir"];
let arr3 = ["Haytham", "Shady", "Mahmoud"];

// Play With Arrays To Prepare For Destructuring
// Write Your Destructuring Assignment Here

let [, a3, b2, , , , c2] = [...arr3, ...arr2, ...arr1];

console.log(`My Best Friends: ${a3}, ${b2}, ${c2}`);

// My Best Friends: Shady, Mahmoud, Ahmed

console.log("-".repeat(20));

const member = {
	age: 30,
	working: false,
	country: "Egypt",
	hobbies: ["Reading", "Swimming", "Programming"],
};

// Write Your Destructuring Assignment Here

let {
	age: a4,
	working: w,
	country: c3,
	hobbies: [h1, , h3],
} = member;

console.log(`My Age Is ${a4} And Iam ${w ? "" : "Not"} Working`);
// My Age Is 30 And Iam Not Working

console.log(`I Live in ${c3}`);
// I Live in Egypt

console.log(`My Hobbies: ${h1} And ${h3}`);
// My Hobbies: Reading And Programming

console.log("-".repeat(20));

const game = {
	title: "YS",
	developer: "Falcom",
	releases: {
		"Oath In Felghana": ["USA", "Japan"],
		"Ark Of Napishtim": {
			US: "20 USD",
			JAP: "10 USD",
		},
		Origin: "30 USD",
	},
};

// Write Your Destructuring Assignment/s Here

let { title: t, developer: d2, releases } = game;

let [o, a5] = Object.keys(releases);

let [u, j] = releases["Oath In Felghana"];

let { US: u_price, JAP: j_price } = releases["Ark Of Napishtim"];

let { Origin: or } = releases;
console.log(`My Favourite Games Style Is ${t} Style`);
// My Favourite Games Style Is YS Style

console.log(`And I Love ${d2} Games`);
// And I Love Falcom Games

console.log(`My Best Release Is ${o} It Released in ${u} & ${j}`);
// My Best Release Is Oath In Felghana It Released in USA & Japan

console.log(`Although I Love ${a5}`);
// Although I Love Ark Of Napishtim

console.log(`${a} Price in USA Is ${u_price}`);
// Ark Of Napishtim Price in USA Is 20 USD

console.log(`${a} Price in Japan Is ${j_price}`);
// Ark Of Napishtim Price in Japan Is 10 USD

console.log(`Origin Price Is ${or}`);
// Origin Price Is 30 USD

console.log("-".repeat(10));

let chosen = 3;

let myFriends = [
	{ title: "Osama", age: 39, available: true, skills: ["HTML", "CSS"] },
	{ title: "Ahmed", age: 25, available: false, skills: ["Python", "Django"] },
	{ title: "Sayed", age: 33, available: true, skills: ["PHP", "Laravel"] },
];

// Write Your Code Here

let [osama, ahmed, sayed] = myFriends;

if (chosen === 1) {
	let {
		title,
		age,
		available,
		skills: [, skillTwo],
	} = osama;

	console.log(title);
	console.log(age);
	console.log(available ? "Avilable" : "Not Avilable");
	console.log(skillTwo);
} else if (chosen === 2) {
	let {
		title,
		age,
		available,
		skills: [, skillTwo],
	} = ahmed;

	console.log(title);
	console.log(age);
	console.log(available ? "Avilable" : "Not Avilable");
	console.log(skillTwo);
} else if (chosen === 3) {
	let {
		title,
		age,
		available,
		skills: [, skillTwo],
	} = sayed;

	console.log(title);
	console.log(age);
	console.log(available ? "Avilable" : "Not Avilable");
	console.log(skillTwo);
}

// If chosen === 1

("Osama");
39;
("Available");
("CSS");

// If chosen === 2

("Ahmed");
25;
("Not Available");
("Django");

// If chosen === 3

("Sayed");
33;
("Available");
("Laravel");
