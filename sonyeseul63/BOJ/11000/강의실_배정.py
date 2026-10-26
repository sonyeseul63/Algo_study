import heapq

N = int(input())
arr = []

for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))

# 강의실 정보
room = []

# 입력받은 강의 정렬 (시작순)
arr.sort()

for start, end in arr:
    if room and room[0] <= start: #확인만하고 빼진 않는다
        heapq.heappop(room)
        heapq.heappush(room, end)
    else:
        heapq.heappush(room, end)

print(len(room))