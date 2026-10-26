n = int(input())
room = []
for _ in range(n):
    x, y = map(int,input().split())
    room.append((x,y))
# 정렬(우선순위): 끝나는 시간 기준, 시작 시간 기준
room.sort(key = lambda room: (room[1], room[0]))
cnt = 0
before = 0
for start, end in room:
    if before <= start:
        cnt += 1
        before = end
print(cnt)