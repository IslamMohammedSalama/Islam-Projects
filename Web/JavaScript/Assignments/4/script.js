// Examples
/* console.log(100_000); // 100000
console.log(100000); // 100000
console.log(5e4 + 5e4); // 100000
 */
// Your Solutions
console.log(Math.pow(10, 5)); // 100000
console.log(1e5); // 100000
console.log(1_00 ** 2 * 10); // 100000
console.log(5e4 * 2); // 100000
console.log(Math.trunc(1_00_000.5)); // 100000
console.log(Math.floor(1_00_000.4)); // 100000
console.log(Math.floor(1_00_000.4)); // 100000
console.log(Math.ceil(99999.999)); // 100000
console.log(parseInt((100000).toFixed(0))); // 100000
console.log(Math.max(500, 100000, 444)); // 100000

console.log(-Number.MIN_SAFE_INTEGER); // 9007199254740991

console.log(`${Number.MAX_SAFE_INTEGER}`.length);

let myVar = "100.56789 Views";

console.log(parseInt(myVar));
console.log(+parseFloat(myVar).toFixed(2));

let num = 10;
console.log(Number.isInteger(num) + Number.isInteger(num));


let flt = 10.4;

console.log(Math.trunc(flt)); // 10
console.log(Math.floor(flt)); // 10
console.log(Math.round(flt)); // 10
console.log(parseInt(flt)); // 10
console.log(+flt.toFixed(0)); // 10

console.log(Math.floor(Math.random() * 5) * 1) // 0 || 1 || 2 || 3 || 4