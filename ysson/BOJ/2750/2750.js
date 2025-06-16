const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

input.shift(); // 첫 줄(N) 제거

input.sort((a, b) => a - b);

for (let num of input) {
    console.log(num);
}