const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const N = Number(input);
let result = 0;

for (let i = 1; i < N; i++) {
    const sum = i + i.toString().split('').reduce((acc, cur) => acc + Number(cur), 0);
    if (sum === N) {
        result = i;
        break;
    }
}

console.log(result);