import sys
input = sys.stdin.readline

n, m = map(int, input().split())
prefixSum = [[0] * (n+1) for _ in range(n+1)]

#전처리-> 입력받는 2차원 리스트를 prefixSum으로
for i in range(1, n+1):
    row = list(map(int, input().split())) # 한줄씩 입력 받으니까
    for j in range(1, n+1):
        prefixSum[i][j] = row[j-1] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = prefixSum[x2][y2] - prefixSum[x1-1][y2] - prefixSum[x2][y1-1] + prefixSum[x1-1][y1-1]
    print(answer)