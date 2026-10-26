while True:
    s = input()
    if s == '.':
        break
    stack = []
    result = "yes"
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        if c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = "no"
                break
        if c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = "no"
                break
    if stack:
        result = "no"
    print(result)