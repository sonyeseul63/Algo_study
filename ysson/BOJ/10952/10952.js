const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

for (let line of input) {
    const [a, b] = line.split(' ').map(Number);
    if (a === 0 && b === 0) break;
    console.log(a + b);
}