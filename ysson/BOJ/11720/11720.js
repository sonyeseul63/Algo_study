const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = input[0];
const numbers = input[1];

let sum = 0;
for (let i = 0; i < N; i++) {
    sum += Number(numbers[i]);
}

console.log(sum);