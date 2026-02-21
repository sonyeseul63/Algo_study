N, M = map(int, input().split())
arr = list(map(int, input().split()))

low = max(arr)
high = sum(arr)
ans = high

def check(size):
    blue = 1
    sum = 0

    for num in arr:
        if sum + num > size:
            sum = 0
            blue += 1
        sum += num

    return blue

while low <= high:
    mid = (low + high) // 2
    
    if check(mid) <= M:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)