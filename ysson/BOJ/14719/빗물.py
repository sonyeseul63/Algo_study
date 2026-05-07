h, w = map(int, input().split())
arr = list(map(int,input().split()))
answer = 0
for i in range(w):
    left = max(arr[:i+1])
    right = max(arr[i:])
    answer += min(left,right) - arr[i]
print(answer)