n = int(input())
arr = list(map(int,input().split()))

stack = []
ans = []

for num in reversed(arr):
    while(stack and stack[-1] <= num): # 같은 값이면 후보 아님
        stack.pop()

    if(not stack):
        ans.append(-1)
    else:
        ans.append(stack[-1])
    
    stack.append(num)

ans.reverse()
print(*ans)
