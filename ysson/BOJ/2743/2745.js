const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

const N = input[0];
const B = parseInt(input[1], 10);

console.log(parseInt(N, B));