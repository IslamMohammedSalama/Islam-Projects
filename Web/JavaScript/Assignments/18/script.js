let prom = prompt("Print Number From - To", "Example: 5-20");

let numOne = parseInt(prom.slice(0, prom.indexOf("-")));
let numTwo = parseInt(prom.slice(prom.indexOf("-")+1));

for (
	let index = numOne < numTwo ? numOne : numTwo;
	index <= ( numOne > numTwo ? numOne : numTwo);
	index++
) {
	console.log(index);
}

let popup = document.querySelector(".popup");
let popupBtn = document.querySelector(".popup .close");

setTimeout(() => {
	popup.classList.add("show");
}, 5000);

addEventListener("click", (ev) => {
	if (ev.target.className === "close") {
		popup.classList.remove("show");
	}
});

let counterOneEle = document.querySelector(".counter-one");

function fcounterOne() {
	counterOneEle.innerHTML -= 1;
	if (parseInt(counterOneEle.innerHTML) === 0) {
		clearInterval(counterOne);
	}
}

let counterOne = setInterval(fcounterOne, 1000);

let counterTwoEle = document.querySelector(".counter-two");

function fcounterTwo() {
	counterTwoEle.innerHTML -= 1;
	if (parseInt(counterTwoEle.innerHTML) === 0) {
		// window.open("https://elzero.org", '_sel', "");
		window.open("https://elzero.org", '_blank', "");
		clearInterval(counterTwo);
	}
}

let counterTwo = setInterval(fcounterTwo, 1000);




let counterThreeEle = document.querySelector(".counter-three");

function fcounterThree() {
	counterThreeEle.innerHTML -= 1;
	if (parseInt(counterThreeEle.innerHTML) === 5) {
		window.open("https://elzero.org", '_blank', "width=500,height=500,left=200,top=200");
		clearInterval(counterThree);
	}
}

let counterThree = setInterval(fcounterThree, 1000);
