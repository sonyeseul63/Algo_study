# “이어지는 중인가?”로 보지 말고
# “각 위치가 시작점이 될 수 있는가?”
T= int(input())
for test_case in range(1, T+1):
    _ = int(input())
    target = input()
    st = input()
    i = 0
    res = 0
    for c in st:
        if c == target[i]:
            i += 1
            if i == len(target):
                res += 1
                i = 0
        elif c == target[0]:
            i = 1
        else:
            i = 0
    print(f"#{test_case} {res}")