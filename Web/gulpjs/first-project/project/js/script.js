const delay = (ms) => new Promise((res) => setTimeout(res, ms));

document.querySelectorAll(".information .info-list li").forEach((element) => {
	element.onclick = async function (event) {
		document.querySelector(".information .info-content div").style.opacity =
			"0";
		await delay(250);
		document.querySelectorAll(".information .info-content div").forEach(
			(ele) =>
				(ele.style.cssText = `
                display:none;
                opacity:0;
                `)
		);
		document
			.querySelectorAll(".information .info-list li")
			.forEach((ele) => ele.classList.remove("selected"));
		element.classList.add("selected");
		document.querySelector(
			`.information .info-content div.${element.dataset.class} `
		).style.display = "block";
		document.querySelector(
			`.information .info-content div.${element.dataset.class} `
		).style.opacity = "1";
	};
});
