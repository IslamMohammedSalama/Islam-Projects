let userName = "Elzero";
console.log(userName.toLowerCase().charAt(0)); // e
console.log(userName.toLowerCase().substr(0,1)); // e
console.log(userName.toLowerCase().slice(0,1)); // e
console.log(userName.toLowerCase().substring(0,1)); // e
console.log(userName.toLowerCase().split("")[0]); // e
console.log(userName[0].toLowerCase().repeat(3)); // eee


let word = "Elzero";
let letterZ = "z";
let letterE = "e";
let letterO = "O";

console.log(word.includes(letterZ)); // True
console.log(word.startsWith(letterE,3)); // True
console.log(word.endsWith(letterO.toLowerCase())); // True