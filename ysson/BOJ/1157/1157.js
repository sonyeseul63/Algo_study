const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().toUpperCase();

const count = {};
for (let ch of input) {
    count[ch] = (count[ch] || 0) + 1;
}

let max = 0;
let answer = '';
let isDuplicate = false;

for (let key in count) {
    if (count[key] > max) {
        max = count[key];
        answer = key;
        isDuplicate = false;
    } else if (count[key] === max) {
        isDuplicate = true;
    }
}

console.log(isDuplicate ? '?' : answer);