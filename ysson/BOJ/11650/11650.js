const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

input.shift(); // 첫 줄(N) 제거

const points = input.map(line => line.split(' ').map(Number));
points.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

for (let [x, y] of points) {
    console.log(x + ' ' + y);
}