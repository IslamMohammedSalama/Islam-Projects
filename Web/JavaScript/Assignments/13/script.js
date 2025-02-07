function getDetails(zName, zAge, zCountry) {
	function namePattern(zName) {
		return `${zName.slice(0, zName.indexOf(" "))}${zName
			.slice(zName.indexOf(" "), zName.indexOf(" ") + 2)
			.toUpperCase()}.`;
	}
	function ageWithMessage(zAge) {
		return `Your Age Is ${parseInt(zAge)}`;
	}
	function countryTwoLetters(zCountry) {
		return zCountry.slice(0, 2).toUpperCase();
	}
	function fullDetails() {
		return `Hello ${namePattern(zName)}, ${ageWithMessage(
			zAge
		)}, You Live On ${countryTwoLetters(zCountry)}`;
	}
	return fullDetails(); // Do Not Edit This
}

console.log(getDetails("Osama Mohamed", "38 Is My Age", "Egypt"));
// Hello Osama M., Your Age Is 38, You Live In EG

console.log(getDetails("Ahmed ali", "32 Is The Age", "Syria"));
// Hello Ahmed A., Your Age Is 32, You Live In SY

console.log("-".repeat(40));

let itsMe = (_) => `Iam A Normal Function`;

console.log(itsMe()); // Iam A Normal Function

let urlCreate = (protocol, web, tld) => `${protocol}://www.${web}.${tld}`;

console.log(urlCreate("https", "elzero", "org")); // https://www.elzero.org

console.log("-".repeat(40));

let checker = (zName) => (status) => (salary) =>
	status === "Available"
		? `${zName}, My Salary Is ${salary}`
		: `Iam Not Avaialble`;

console.log(checker("Osama")("Available")(4000)); // Osama, My Salary Is 4000
console.log(checker("Ahmed")("Not Available")()); // Iam Not Avaialble

console.log("-".repeat(40));

function specialMix(...data) {
	let result = 0;

	for (let index = 0; index < data.length; index++) {
		if (isNaN(parseInt(data[index])) !== false) {
			continue;
		} else {
			result += parseInt(data[index]);
		}
	}
	if (result === 0) return "All Is String";
	return result;
}

console.log(specialMix(10, 20, 30)); // 60
console.log(specialMix("10Test", "Testing", "20Cool")); // 30
console.log(specialMix("Testing", "10Testing", "40Cool")); // 50
console.log(specialMix("Test", "Cool", "Test")); // All Is Strings
