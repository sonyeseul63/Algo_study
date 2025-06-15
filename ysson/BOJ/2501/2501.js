const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

const [N, K] = input;
let count = 0;
let answer = 0;

for (let i = 1; i <= N; i++) {
    if (N % i === 0) {
        count++;
        if (count === K) {
            answer = i;
            break;
        }
    }
}

console.log(answer);