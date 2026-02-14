#for로 N번 입력받는데(), 나올때마다 힙에 넣고 
#숫자가 0이면 우선순위 큐로 출력, 그다음 숫자도 for문 실행,
#출력할때 출력할게 없으면 0 출력
# 고민할 거는 값과 인덱스.. 우선순위 큐에는 일단 값이 들어가야함
#우선순위 큐는 push할때 기준을 넘겨주고 pop은 그냥 하면된다
import heapq
N = int(input().strip())

heap = []

for _ in range(N):
    n = int(input().strip())
    if(n == 0): 
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1]) #문법 조심
    
    else:
        heapq.heappush(heap, (abs(n), n))