import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        f1 = heapq.heappop(scoville)
        f2 = heapq.heappop(scoville)
        mix = f1 + (f2 * 2)
        if mix == 0:
            return -1
        else:
            heapq.heappush(scoville, mix)
            answer += 1
    return answer