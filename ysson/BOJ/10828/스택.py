num = int(input())

stack = []
for _ in range(num):
    cmd = list(input().split()) # 명령어는 cmd[0], 숫자는 cmd[1]
    if cmd[0] == 'push':
        stack.append(cmd[1])
    if cmd[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1)
    if cmd[0] == 'size':
        print(len(stack))
    if cmd[0] == 'empty':
        if not stack: print(1)
        else: print(0)
    if cmd[0] == 'top':
        if stack: print(stack[-1])
        else: print(-1)