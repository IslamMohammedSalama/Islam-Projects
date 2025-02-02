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

