import heapq

heap = []
result = []
N = int(input())

for _ in range(N):
    n = int(input())
    if n == 0:
        if not heap:
            result.append(0)
        else:
            result.append(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(n), n))

print("\n".join(map(str,result)))