let req = new XMLHttpRequest();
req.open("GET", "articals.jsonc", true);
req.send();
let mainData = "";
let updatedData = "";
req.onreadystatechange = function () {
	if (this.readyState === 2) {
		console.log("JSON Object Content Here");
	}
	if (this.readyState === 4 && this.status === 200) {
		console.log("Data Loaded");
		mainData = JSON.parse(req.responseText);
		console.log(mainData);
		console.log("---------------------------------");
		mainData.forEach((element) => {
			element["category"] = "All";
		});
		updatedData = JSON.stringify(mainData);
		console.log(updatedData);
		console.log("JSON Object Content Here");
		let data = document.createElement("div");
		data.id = "data";
		mainData.forEach((element) => {
			let block = document.createElement("div");
			let h2 = document.createElement("h2");
			h2.innerHTML = `${element["title"]}`;
			let p1 = document.createElement("p");
			p1.innerHTML = `${element["body"]}`;
			let p2 = document.createElement("p");
			p2.innerHTML = `Author: ${element["author"]}`;
			let p3 = document.createElement("p");
			p3.innerHTML = `Category: ${element["category"]}`;
			block.appendChild(h2);
			block.appendChild(p1);
			block.appendChild(p2);
			block.appendChild(p3);
			data.appendChild(block);
		});
		document.body.appendChild(data);
	}
};
