from collections import Counter

n = int(input())
cards = Counter(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

# print(*[cards[f] for f in find])
print(" ".join(str(cards[f]) for f in find)) #join이 하나씩 꺼내줌(소비)