# dict 사용
n = int(input())
cards = list(map(int, input().split()))
d = {}
for c in cards:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

m = int(input())
ans = []
find = list(map(int, input().split()))
for f in find:
    #키가 없으면 에러
    # if f in d:
    #     ans.append(d[f])
    # else: 
    #     ans.append(0)
    ans.append(d.get(f, 0))
print(*ans)