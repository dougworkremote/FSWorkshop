// the primary data structures in JS are arrays and objects
// if youre familiar w/ the idea of lists or sequences, arrays are the similar here
// objects would be like maps, or hash maps

// there are diff ways to create an array or obj
// using 'literal' syntax is the most common
// [val, ...valN] for arrays
// { 'prop':val, ...propN } for objects

const listOfAnimalTypes = ['cats', 'dogs', 'lizards', 'dinos', 'hippos']

// JS is really flexible when it comes to working w/ objects
const singleDino = {
    'name': 'T-Rex',
    'aggression': 7,
    'coolness': 10
}
singleDino.name = 'Raptor';
singleDino['name'] = 'Triceratops';

const otherDino = {
    name: 'T-Rex',
    aggression: 7,
    coolness: 10,
    avgAggroCool: function() {
        return ((this.aggression + this.coolness) / 2);
    }
}

const aggroCoolCalc = otherDino.avgAggroCool();
console.log(aggroCoolCalc);

// in JS, everything is an obj
// obj are used for building things youll manipulate
// the bedrock for JS
