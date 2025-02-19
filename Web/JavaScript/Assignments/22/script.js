let ip = "2001:db8:3333:4444:5555:6666:7777:8888";

let reOne = /(\d+|\D+)+/ig

console.log(ip.match(reOne))


let specialNames = "Os10O OsO Os100O Osa100O Os1000 Os100m";

let reTwo = /Os(\d+)?o/ig

console.log(specialNames.match(reTwo))

// Output
// ['Os10O', 'OsO', 'Os100O']

let phone = "+(995)-123 (4567)";

let reThree = /\+\(\d{3}\)-\d{3} \(\d{4}\)/g;

console.log(phone.match(reThree));


// let re = /https?:\/\/(?:[-\w]+\.)?([-\w]+)\.\w+(?:\.\w+)?\/?.*/i;
// let re = /(https?:\/\/)?([\w]+\.)?([\w]+)\.\w+(\.\w+)?\/?.*/ig;


let date1 = "25/10/1982";
let date2 = "25 - 10 - 1982";
let date3 = "25 10 1982";
let date4 = "25 10 82";

let reFour = /\d{2}((\s-\s)|(\/)|\s)\d+((\s-\s)|(\/)|\s)\d{2,4}/ig; // Write Pattern Here

console.log(date1.match(reFour)); // "25/10/1982"
console.log(date2.match(reFour)); // "25 - 10 - 1982"
console.log(date3.match(reFour)); // "25 10 1982"
console.log(date4.match(reFour)); // "25 10 82"



let url1 = 'elzero.org';
let url2 = 'http://elzero.org';
let url3 = 'https://elzero.org';
let url4 = 'https://www.elzero.org';
let url5 = 'https://www.elzero.org:8080/articles.php?id=100&cat=topics';

let re = /(https?:\/\/)?(www.)?\w+.\w+(:\d*)?(\/\w+.\w+\D+\w+\D+)?/ig; // Write Your Pattern Here

console.log(url1.match(re));
console.log(url2.match(re));
console.log(url3.match(re));
console.log(url4.match(re));
console.log(url5.match(re));