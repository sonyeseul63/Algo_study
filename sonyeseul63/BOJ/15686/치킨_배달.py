from itertools import combinations

N, M = map(int, input().split())
homes, chickens = [], []

# 입력받은 좌표에 다라 homes, chickens 좌표 리스트 구하기
# 각각의 좌표리스트를 왜? 치킨집의 콤보를 뽑고, 집집마다의 거리를 구해야 하기 때문
for i in range(N):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v == 1:
            homes.append((i, j))
        elif v == 2:
            chickens.append((i, j))

answer = None

# 치킨집의 조합들 순회
for combo in combinations(chickens, M):
    total = sum(
        min(abs(home[0] - c[0]) + abs(home[1] - c[1]) for c in combo)
        for home in homes
    )
    if answer is None or total < answer:
        answer = total
print(answer)