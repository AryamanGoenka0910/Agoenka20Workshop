// Team Reverse: Aryaman Goenka, Haotian Gan
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08
// --------------------------------------------------

//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;

//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//getElemenetByTagName(<Tag>)
//getElementsByClassName(<Class>)

//.addEventListener(<Event>, <Function>)
//document.createElement(<HTML Tag Value>)
//element.remove()
//element.innerHtml
//element.appendChild(<Element>)

//element.setAttribute(<Name>, <Value>)
//element.getAttributee(<Name>)

//insert your implementations here for...
// FIB
// FAC
// GCD

function fact(n){
  if (n == 0){
      return 1;
  }
  else {
      return fact(n-1) * n;
  }
}

function fib(n){
  if (n <= 1){
      return 1;
  }
  else{
      return fib(n - 1) + fib(n - 2);
  }
}

function greatestcf(a, b){
  gcf = 0;
  for (let i = 1; i < a + 1; i++){
      if (a % i == 0){
          if (b % i == 0){
              gcf = i;
      }
    }
  }
  return gcf;
}


