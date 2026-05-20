T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    #  어떤게 먼저일까? 무게랑 적재용량이랑..
    w.sort(reverse = True)
    t.sort()
    cnt = 0
    for i in w:
        if t and t[-1] >= i:
            t.pop()
            cnt += i
    print(f"#{test_case} {cnt}")
