#섞은 음식의 스코빌 지수 = 가장 안매운 + (두 번째로 안매운 * 2) -> 최솟값 출력 
#출력: 섞어야 하는 최소 횟수
#안되는 경우: 음식 1개만 남았는데 K미만 -> -1

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            break
        else:
            new = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville, new)
            answer += 1
    
    
    return answer