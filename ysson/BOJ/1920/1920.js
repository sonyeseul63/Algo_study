const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const A = new Set(input[1].split(' ').map(Number));
const M = Number(input[2]);
const nums = input[3].split(' ').map(Number);

for (let num of nums) {
    console.log(A.has(num) ? 1 : 0);
}