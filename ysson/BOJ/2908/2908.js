const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

const reversed = input.map(num => num.split('').reverse().join(''));
console.log(Math.max(...reversed.map(Number)));