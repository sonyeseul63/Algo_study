case = int(input())
for _ in range(case):
    n = int(input())
    d = {}
    for _ in range(n):
        item, category = input().split()
        d[category] = d.get(category, 0) + 1

    comb = 1
    for n in d.values():
        comb *= (n + 1)
    print(comb - 1)
