"use strict";

// this is a normal function
function func1() {
    console.log('func1');
}

// this function (func, fn, f) takes 1 param
function func2(str) {
    console.log('func2');
    console.log(str);
}

// this one takes 2
// str is short for 'string'
function func3(fn, str) {
    console.log('func3');
    // were actually calling the passed fn inside func3 w/ the 2nd argument
    // fn is a callback
    fn(str);
}

// calling func3 w/ func2, which logs a str, w/ str 'hello'
func3(func2, 'hello');

// JS has 1st class functions
// which can be assigned, returned, and passed like parameters/arguments

function func4(str) {
    console.log('func4');
    return function() { // this is an anonymous func because it doesn't have a name
        console.log(str);
    }
}

const func4ex = func4('hello2'); // func4 actually returned a func
func4ex(); // we are executing that returned func here

// recursion
function factorial(n) {
    if (n == 0) {return 1;}
    return (n * factorial(n - 1));
}
let fac8 = factorial(8);
console.log(fac8);
