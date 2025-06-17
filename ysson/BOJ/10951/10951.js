const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

for (let line of input) {
    if (line === '') continue;
    const [a, b] = line.split(' ').map(Number);
    if (!isNaN(a) && !isNaN(b)) {
        console.log(a + b);
    }
}