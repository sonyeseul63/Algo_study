const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const x = input[0];
const y = input[1];

if (x > 0 && y > 0) {
    console.log(1);
} else if (x < 0 && y > 0) {
    console.log(2);
} else if (x < 0 && y < 0) {
    console.log(3);
} else {
    console.log(4);
}