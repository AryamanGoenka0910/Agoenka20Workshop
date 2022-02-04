// Team Last-Row:: Aryaman Goenka, Tomas Acuna
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2022-02-03
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

function fib(n){
    if (n <= 1){
        return 1;
    }
    else{
        return fib(n - 1) + fib(n - 2);
    }
}

console.log(fib(5))
console.log(fib(6))
console.log(fib(7))