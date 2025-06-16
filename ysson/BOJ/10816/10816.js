const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const cards = input[1].split(' ').map(Number);
const M = Number(input[2]);
const nums = input[3].split(' ').map(Number);

const countMap = new Map();
for (let card of cards) {
    countMap.set(card, (countMap.get(card) || 0) + 1);
}

let result = [];
for (let num of nums) {
    result.push(countMap.get(num) || 0);
}

console.log(result.join(' '));