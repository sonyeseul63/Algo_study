import heapq
def solution(jobs):
    answer = 0
    
    t = 0 #시간
    hq = []
    i = 0 #큐에 넣은 인덱스
    cnt = 0 #실행시킨 횟수
    end_sum = 0
    jobs.sort()
    
    # 컨트롤러 선택해서 실행시키는 반복문
    while cnt < len(jobs):
        # 해당시간까지 작업이 있으면 담기
        while i < len(jobs) and jobs[i][0] <= t:
            start, length = jobs[i]
            heapq.heappush(hq, (length, start, i))
            i += 1
            
        if hq:
            length, start, idx = heapq.heappop(hq)
            t += length
            end_sum += (t-start)
            cnt += 1
        
        else:
            t = jobs[i][0]
        
    answer = end_sum // len(jobs)
    
    return answer