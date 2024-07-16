let body = document.querySelector('main');
body.style.overflowY = 'auto';
body.style.width = '100%';
body.style.height = '100%';
body.style.padding = '35px 15px';
body.style.borderTop = '1px solid #ddd';

let egypt_flag = document.createElement('img');
egypt_flag.src = 'images/egypt-flag.svg';
egypt_flag.style.width = '100%';
egypt_flag.style.height = '100vh';
egypt_flag.style.marginTop = "10px"

body.appendChild(egypt_flag);

let container = document.createElement('div');

container.style.width = '100%';
container.style.height = '100vh';
container.style.backgroundColor = 'white';
container.style.position = 'relative';
body.appendChild(container);

let black = document.createElement('div');
black.style.position = 'absolute';
black.style.width = '100%';
black.style.top = '0';
black.style.height = '33.333%';
black.style.backgroundColor = 'black';
container.appendChild(black);

let green = document.createElement('div');
green.style.position = 'absolute';
green.style.width = '100%';
green.style.bottom = '0';
green.style.height = '33.333%';
green.style.backgroundColor = 'green';
container.appendChild(green);

let red = document.createElement('div');
red.style.position = 'absolute';
red.style.borderStyle = 'solid';
red.style.borderColor = 'transparent transparent transparent red';
red.style.borderWidth = '50vh';

container.appendChild(red);

