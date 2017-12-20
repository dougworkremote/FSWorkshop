"use strict";

// + - * / %
let a = 3;
let b = 6;
let c = a + b;
let d = b - a;
let e = a * c;
let f = e / a;
let g = 12 % d; // modulus = remainder

// if/elseif/else < > <= >= == != === !==
if (a < b) {console.log('a < b')}
if (a > b) {console.log('should never happen')}
let h = 3;
if (a === h) {console.log('these are exactly equal')}
if (a) {console.log('eval to true')}
let i = 4;
if (a > b) {
    console.log('a was reassigned');
} else if (a < b) {
    console.log('a might have its original val')
} else {
    console.log('something else happened to a')
}

// || && !
if (a < b && e > c) {console.log('math is working, yay!')}
if (a > b || b > a) {console.log('well the second one is true')}
// ! is negation
if (!a) {console.log('will this log?')}
let j = false;
if (!j) {console.log('what about this?')}
if (!!j) {console.log('this?')}

// loops
for (let i = 0; i < 5; i++) {
    // doing some iterative processing here
}
