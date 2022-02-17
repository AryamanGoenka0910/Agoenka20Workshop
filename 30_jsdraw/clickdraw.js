//retrieve node in DOM via ID
var c = document.getElementById('slate');

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect"){
        mode = "arc"
    }
    else{
        mode = "rect"
    }
}

var drawRect = (e) => {
    console.log("draw rect");
    mouseX = e.offsetX;
    mouseY = e.offsetY;
    ctx.fillRect(mouseX, mouseY, 50, 90)
    console.log("mouseclick registered at ", mouseX, mouseY);
}

//var drawCicle = function(e){
var drawCircle = (e) => {
    console.log("draw circ");
    mouseX = e.offsetX;
    mouseY = e.offsetY;
    ctx.beginPath()
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.fill()
    console.log("mouseclick registered at", mouseX, mouseY);
}

//var draw = function(e){
var draw = (e) => {
    console.log("drawing");
    if (mode === "rect"){ 
        drawRect(e); 
    }
    else{
        drawCircle(e);
    }
}

//var wipeCanvas = function(){
var wipeCanvas = (e) => {
    console.log("wipe");
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);

var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);



/*
TOOLBOX:
clearRect()
getElementByID()
addEventListener()
fillStyle()
strokeStyle()
clearRect()
fillText()
beginPath()
fillStyle
arc()
fill()
stroke()
Math.PI
offsetX
offsetY
*/