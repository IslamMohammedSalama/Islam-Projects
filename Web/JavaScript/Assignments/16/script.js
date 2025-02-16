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

// let oneTitle = two.title;
// let twoTitle = one.title;

// let oneContent = two.textContent;
// let twoContent = one.textContent;

// Shaffile Titles

// one.title = twoTitle;
// two.title = oneTitle;

// New Way
[one.title, two.title] = [two.title, one.title];

// Shaffile Content
// one.textContent = oneContent;
// two.textContent = twoContent;

// New Way
[one.textContent, two.textContent] = [two.textContent, one.textContent];

let newImgs = document.querySelectorAll(".newimgs img");

for (let index = 0; index < newImgs.length; index++) {
	if (newImgs[index].alt === "") {
		newImgs[index].alt = "Elzero New";
	} else {
		newImgs[index].alt = "Old";
	}
}

// The Assignment Is Incomplated so I Will Complate It Tomorrow

let form = document.createElement("form");

form.method = "post";
form.style.display = "flex";
form.style.flexDirection = "column";
form.style.width = "600px";
form.style.gap = "10px";
form.style.margin = "15px auto";
form.style.borderRadius = "10px";
form.style.padding = "20px";

let numOfEles = document.createElement("input");
numOfEles.type = "number";
numOfEles.name = "elements";
numOfEles.className = "input";
numOfEles.placeholder = "Number Of Elements";
numOfEles.style.padding = "5px";
numOfEles.style.padding = "10px";
numOfEles.style.borderColor = "#eee";
numOfEles.style.borderRadius = "10px";

let elesText = document.createElement("input");
elesText.type = "text";
elesText.name = "texts";
elesText.className = "input";
elesText.placeholder = "Text Of Elements";
elesText.style.padding = "5px";
elesText.style.padding = "10px";
elesText.style.borderColor = "#eee";
elesText.style.borderRadius = "10px";

let selectElesType = document.createElement("select");
selectElesType.className = "input";
selectElesType.name = "type";
selectElesType.style.padding = "10px";
selectElesType.style.borderColor = "#eee";
selectElesType.style.borderRadius = "10px";

let optOne = document.createElement("option");
optOne.innerHTML = "Section";
optOne.value = "section";
let optTwo = document.createElement("option");
optTwo.innerHTML = "Div";
optTwo.value = "div";

let submit = document.createElement("input");
submit.type = "submit";
submit.name = "create";
submit.value = "Create";
submit.style.backgroundColor = "#009090";
submit.style.border = "none";
submit.style.outline = "none";
submit.style.padding = "10px";
submit.style.borderRadius = "50px";
submit.style.color = "white";
submit.style.fontWeight = "bold";
submit.style.cursor = "pointer";

let results = document.createElement("div");
results.style.display = "grid";
results.style.gridTemplateColumns = "repeat(3,30%)";
results.style.gap = "20px";

submit.onclick = function (event) {
	event.preventDefault();
	if (selectElesType.value === "section") {
		results.innerHTML = "";
		for (let index = 0; index < parseInt(numOfEles.value); index++) {
			let box = document.createElement("section");
			box.style.display = "flex";
			box.style.justifyContent = "center";
			box.style.alignItems = "center";
			box.style.backgroundColor = "#fc5303";
			box.style.borderRadius = "10px";
			box.style.color = "white";
			box.id = `id-${index}`;
			box.title = "Element";
			box.style.padding = "20px";
			box.innerHTML = elesText.value;
			results.appendChild(box);
		}
	} else {
		results.innerHTML = "";
		for (let index = 0; index < parseInt(numOfEles.value); index++) {
			let box = document.createElement("div");
			box.style.display = "flex";
			box.style.justifyContent = "center";
			box.style.alignItems = "center";
			box.style.backgroundColor = "#009000";
			box.style.borderRadius = "10px";
			box.style.color = "white";
			box.style.padding = "20px";
			box.id = `id-${index}`;
			box.title = "Element";
			box.innerHTML = elesText.value;
			results.appendChild(box);
		}
	}
};

document.body.appendChild(form);
form.appendChild(numOfEles);
form.appendChild(elesText);
form.appendChild(selectElesType);
selectElesType.appendChild(optOne);
selectElesType.appendChild(optTwo);

form.appendChild(submit);
form.appendChild(results);
