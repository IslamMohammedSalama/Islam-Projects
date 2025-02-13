let addInput = document.querySelector(".classes-to-add");
let removeInput = document.querySelector(".classes-to-remove");
let current = document.querySelector(`[title="Current"]`);
let classesList = document.querySelector(`.classes-list div`);

function addOrRemove() {
	// remove all elements at the start
	document.querySelectorAll("span").forEach((el) => el.remove());

	for (let index = 0; index < this.value.trim().split(" ").length; index++) {
		if (addInput.value) {
			for (
				let index = 0;
				index < addInput.value.trim().toLowerCase().split(" ").length;
				index++
			) {
				current.classList.add(
					addInput.value.trim().toLowerCase().split(" ")[index]
				);
			}
		} else if (removeInput.value) {
			for (
				let index = 0;
				index < removeInput.value.trim().toLowerCase().split(" ").length;
				index++
			) {
				current.classList.remove(
					removeInput.value.trim().toLowerCase().split(" ")[index]
				);
			}
		}
	}

	this.value = "";

	if (current.classList.length) {
		classesList.textContent = "";

		[...current.classList].sort().forEach((el) => {
			let clSpan = document.createElement("span");
			clSpan.textContent = el;
			classesList.append(clSpan);
		});
	} else {
		classesList.textContent = "No Classes To Show";
	}
}

addInput.onblur = addOrRemove;
removeInput.onblur = addOrRemove;

window.onload = () => {
	if (current.classList.length) {
		classesList.textContent = "";

		[...current.classList].sort().forEach((el) => {
			let clSpan = document.createElement("span");
			clSpan.textContent = el;
			classesList.append(clSpan);
		});
	} else {
		classesList.textContent = "No Classes To Show";
	}
};

let divOne = document.createElement("div");
divOne.title = "Start Element";
divOne.className = "start";
divOne.setAttribute("data-value", "Start");
divOne.textContent = "Start";

let divTwo = document.createElement("div");
divTwo.title = "End Element";
divTwo.className = "end";
divTwo.setAttribute("data-value", "end");
divTwo.textContent = "End";

document.querySelector(".assign-two").lastElementChild.remove();
document.querySelector(".assign-two").before(divOne);
document.querySelector(".assign-two").after(divTwo);

console.log(
	document.querySelector("body > div:has(span)").lastChild.textContent.trim()
);

window.addEventListener("click", (e) => {
    console.log(`This Is ${e.target.nodeName}`)
});
