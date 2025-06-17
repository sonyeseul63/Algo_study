const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
let count = 0;

for (let i = 1; i <= N; i++) {
    const word = input[i];
    let isGroup = true;
    const seen = new Set();
    let prev = '';

    for (let ch of word) {
        if (ch !== prev) {
            if (seen.has(ch)) {
                isGroup = false;
                break;
            }
            seen.add(ch);
        }
        prev = ch;
    }

    if (isGroup) count++;
}

console.log(count);