const delay = (ms) => new Promise((res) => setTimeout(res, ms));

let button = document.querySelector("button");
// button.onclick = function (e) {};
window.addEventListener("mousedown", (e) => {
	const target = e.target;

	if (target.nodeName == "BUTTON") {
		show_ripple(target);
		// console.log("Yes")
	}
});
function show_ripple(button) {
	const style = getComputedStyle(button);
	let ripple_elmnt = document.createElement("span");
	let diameter = Math.max(parseInt(style.height), parseInt(style.width)) * 1.5;
	let radius = diameter / 2;

	ripple_elmnt.className = "ripple";
	ripple_elmnt.style.height = ripple_elmnt.style.width = diameter + "px";
	ripple_elmnt.style.position = "absolute";
	ripple_elmnt.style.borderRadius = "50%";
	ripple_elmnt.style.pointerEvents = "none";

	ripple_elmnt.style.left = event.clientX - button.offsetLeft - radius + "px";
	ripple_elmnt.style.top = event.clientY - button.offsetTop - radius + "px";

	ripple_elmnt.style.transform = "scale(0)";
	ripple_elmnt.style.transition = "transform 1s ease, opacity 0.5s ease";
	ripple_elmnt.style.background = "rgba(255,255,255,0.5)";
	button.appendChild(ripple_elmnt);

	setTimeout(async () => {
		ripple_elmnt.style.transform = "scale(5)";
		ripple_elmnt.style.opacity = 0;
		await delay(500);
		button.removeChild(ripple_elmnt);
	}, 10);

	setTimeout(() => {
		try {
			// button.removeChild(ripple_elmnt);
		} catch (er) {}
	}, 400);
	// button.addEventListener(
	// 	"mouseup",
	// 	(e) => {
	// 		ripple_elmnt.style.opacity = 0;
	// 		setTimeout(() => {
	// 			try {
	// 				button.removeChild(ripple_elmnt);
	// 			} catch (er) {}
	// 		}, 400);
	// 	},
	// 	{ once: true }
	// );
	// button.addEventListener(
	// 	"blur",
	// 	(e) => {
	// 		ripple_elmnt.style.opacity = 0;
	// 		setTimeout(() => {
	// 			try {
	// 				button.removeChild(ripple_elmnt);
	// 			} catch (er) {}
	// 		}, 450);
	// 	},
	// 	// { once: true }
	// );
}
