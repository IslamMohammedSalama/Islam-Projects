function getData(link) {
	return new Promise((res, rej) => {
		let newReq = new XMLHttpRequest();
		newReq.onload = function () {
			if (this.readyState === 4 && this.status === 200) {
				res(JSON.parse(this.responseText));
			} else {
				rej(Error("No Data Found , Or Link Is Wrong"));
			}
		};
		newReq.open("POST", link);
		newReq.send();
	});
}

getData("data.jsonc")
	.then(
		(resVal) => {
			resVal.length = 5;
			return resVal;
		},
		(rejVal) => document.write("No Data Found")
	)
	.then(
		(resValTwo) => {
			for (let index = 0; index < resValTwo.length; index++) {
				let mainDiv = document.createElement("div");
				let h2 = document.createElement("h2");
				h2.innerText = `${resValTwo[index]["title"]}`;
				let p = document.createElement("p");
				p.innerText = `${resValTwo[index]["description"]}`;
				mainDiv.append(h2, p);
				document.body.appendChild(mainDiv);
			}
		},
		(rejValTwo) => document.write("No Data Found")
	);

fetch("data.jsonc")
	.then((resVal) => {
		return resVal.json();
	})
	.then((resValTwo) => {
		document.write(`-`.repeat());
		for (let index = 0; index < resValTwo.length; index++) {
			let mainDiv = document.createElement("div");
			let h2 = document.createElement("h2");
			h2.innerText = `${resValTwo[index]["title"]}`;
			let p = document.createElement("p");
			p.innerText = `${resValTwo[index]["description"]}`;
			mainDiv.append(h2, p);
			document.body.appendChild(mainDiv);
		}
	});
