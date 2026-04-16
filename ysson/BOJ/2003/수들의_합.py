n, m = map(int, input().split())

arr = list(map(int, input().split()))

# 카운터
cnt = 0

# 초기 합
sum = 0

# 투 포인터: 구간의 양 끝
left = 0

# 순회
for right in range(n):
    sum += arr[right]

    while sum > m: # sum 이 작거나 커질때 까지 (초건 충족 x, 빠르게 left 옮기기)
        sum -= arr[left]
        left += 1
    
    if sum == m:
        cnt += 1

print(cnt)
