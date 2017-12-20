"use strict";

const el_total = document.getElementById('running_total');
const el_add_btn = document.getElementById('counter_add');
const el_subtract_btn = document.getElementById('counter_subtract');
let counter_tally;

if (!el_total.innerHTML) {
    counter_tally = 0;
    el_total.innerHTML = counter_tally;
}

el_add_btn.addEventListener('click', function() {
    el_total.textContent = ++counter_tally;
});
el_subtract_btn.addEventListener('click', function() {
    if (counter_tally >= 1) {el_total.textContent = --counter_tally;}
});
