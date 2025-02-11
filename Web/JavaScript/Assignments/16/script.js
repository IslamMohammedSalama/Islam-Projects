let s1 = document.getElementById("elzero");
let s2 = document.getElementsByClassName("element");
let s3 = document.getElementsByTagName("div");
let s4 = document.getElementsByName("js");
let s5 = document.querySelector("[id='elzero']");
let s6 = document.querySelector("[class='element']");
let s7 = document.querySelector("[name='js']");
let s8 = document.querySelector(".element");
let s9 = document.querySelectorAll("[id='elzero']");
let s10 = document.querySelectorAll(".element");
let s11 = document.querySelectorAll("[class='element']");
let s12 = document.querySelector("[name='js']");
let s13 = document.body.firstChild;
let s14 = document.body.lastChild;
let s15 = document.body.children[0];

let imgs = document.querySelectorAll(".imgs img");

for (let index = 0; index < imgs.length; index++) {
	imgs[index].alt = "Elzero Logo";
	imgs[index].src = "https://elzero.org/wp-content/themes/elzero/imgs/logo.png";
	imgs[index].style.backgroundColor = "black";
}

let input = document.querySelector("form input");
let result = document.querySelector("form .result");

input.oninput = function () {
	result.innerHTML = `{${input.value}} USD Dollar = {${(
		input.value * 15.6
	).toFixed(2)}} Egyptian Pound`;
};

let one = document.querySelector(".one");
let two = document.querySelector(".two");

let oneTitle = two.title;
let twoTitle = one.title;

let oneContent = two.textContent;
let twoContent = one.textContent;
// Shaffile Titles

one.title = twoTitle;
two.title = oneTitle;

// Shaffile Content
one.textContent = oneContent;
two.textContent = twoContent;

let newImgs = document.querySelectorAll(".newimgs img");

for (let index = 0; index < newImgs.length; index++) {
	if (newImgs[index].alt === "") {
		newImgs[index].alt = "Elzero New";
	} else {
		newImgs[index].alt = "Old";
	}
}


// The Assignment Is Incomplated so I Will Complate It Tomorrow