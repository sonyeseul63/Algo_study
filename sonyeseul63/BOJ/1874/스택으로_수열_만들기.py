n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

pushNum = 1
stack = []
ans = []

for num in arr:
    while(pushNum <= num):
        stack.append(pushNum)
        ans.append("+")
        pushNum+=1

    if(stack and stack[-1] == num):
        stack.pop()
        ans.append("-")

    else: 
        print("NO")
        break
else:
    print("\n".join(ans))