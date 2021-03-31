// thank you Igor Agapov for the code pen that inspired this script.
// view the source here: https://codepen.io/harryheman/pen/ZEEPRba

const container = document.getElementById('nav-container');
const C = document.getElementById("matrix"),
  $ = C.getContext("2d"),
  W = (C.width = window.innerWidth),
  H = (C.height = container.offsetHeight);

const str = "$$$€¥₤£¢¢  ₢₡₠৳  ฿฿฿¤₣₴  ₰₪₲₳  ₯₱₥₫",
matrix = str.split("");

let font = 15,
  col = W / font,
  arr = [];

for (let i = 0; i < col; i++) arr[i] = 1;

function draw() {
  $.fillStyle = "rgba(0,0,0,.05)";
  $.fillRect(0, 0, W, H);
  $.fillStyle = "#0f0";
  $.font = font + "px system-ui";
  for (let i = 0; i < arr.length; i++) {
    let txt = matrix[Math.floor(Math.random() * matrix.length)];
    $.fillText(txt, i * font, arr[i] * font);
    if (arr[i] * font > H && Math.random() > 0.975) arr[i] = 0;
    arr[i]++;
  }
}

setInterval(draw, 123);

window.addEventListener("resize", () => location.reload());