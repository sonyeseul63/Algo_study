const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, S] = input[0].split(' ').map(Number);
const nums = input[1].split(' ').map(Number);

let count = 0;

function dfs(idx, sum) {
    if (idx === N) return;
    if (sum + nums[idx] === S) count++;
    dfs(idx + 1, sum + nums[idx]);
    dfs(idx + 1, sum);
}

dfs(0, 0);

console.log(count);