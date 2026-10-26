n = int(input())
arr = list(map(int, input().split()))
arr.sort()
w = 0
res = 0
for i in range(len(arr)):
    a = arr[i]
    w += a
    res += w
print(res)