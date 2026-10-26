n, m = map(int, input().split())
arr = list(map(int, input().split()))

# arr 전처리 -> sumArr(구간합)
sumArr = [0]
for z in range(n):
    sumArr.append(sumArr[z] + arr[z])

for _ in range(m):
    i, j = map(int, input().split())
    print(sumArr[j] - sumArr[i-1])