let fontFamily = document.querySelector(".font-family");
let fontSize = document.querySelector(".font-size");
let bgColor = document.querySelector(".bg-color");

fontFamily.onchange = () => {
	localStorage.setItem("font-family", fontFamily.value);
	document.body.style.fontFamily = `${fontFamily.value}`;
};

fontSize.onchange = () => {
	localStorage.setItem("font-size", fontSize.value);
	document.body.style.fontSize = fontSize.value;
};

bgColor.onchange = () => {
	localStorage.setItem("bg-color", bgColor.value);
	document.body.style.backgroundColor = `${bgColor.value}`;
};

document.body.style.fontFamily = localStorage.getItem("font-family");
document.body.style.fontSize = localStorage.getItem("font-size");
document.body.style.backgroundColor = localStorage.getItem("bg-color");
fontSize.value = localStorage.getItem("font-size");
bgColor.value = localStorage.getItem("bg-color");
fontFamily.value = localStorage.getItem("font-family");

// ---------------------------------------------------------------------------------------------------------------------

let text = document.querySelector("[type='text']");
let number = document.querySelector("[type='number']");
let password = document.querySelector("[type='password']");

let aiV = document.querySelector(".ai-v");

text.onblur = () => {
	sessionStorage.setItem("text", text.value);
};

number.onblur = () => {
	sessionStorage.setItem("number", number.value);
};

password.onblur = () => {
	sessionStorage.setItem("password", password.value);
};

aiV.onchange = () => {
	sessionStorage.setItem("ai-v", aiV.value);
};

if (sessionStorage.getItem("text")) {
	text.value = sessionStorage.getItem("text");
}

if (sessionStorage.getItem("number")) {
	number.value = sessionStorage.getItem("number");
}

if (sessionStorage.getItem("password")) {
	password.value = sessionStorage.getItem("password");
}

if (sessionStorage.getItem("ai-v")) {
	aiV.value = sessionStorage.getItem("ai-v");
}
