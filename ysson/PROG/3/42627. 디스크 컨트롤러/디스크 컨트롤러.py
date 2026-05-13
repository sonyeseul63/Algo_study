import heapq
def solution(jobs):
    jobs.sort()
    answer = 0
    works = []
    times = 0 #시간의 흐름
    avg_sum = 0 #평균내기 합
    idx = 0 # job 처리 인덱스
    cnt = 0

    # 일단 하나는 처리하는 반복문
    while cnt < len(jobs):
        # 해당 시간안에 온 것 큐 넣기
        while idx < len(jobs) and jobs[idx][0] <= times:
            (s, l) = jobs[idx]
            heapq.heappush(works, (l, s, idx))
            idx += 1
        
        # 하나 빼서 작업 실행
        if works:
            l, s, i = heapq.heappop(works)
            times += l
            avg_sum += times - s
            cnt +=1
            
        # 해당 시간 안에 들어온 작업이 없다 -> 첫번쨰로 들어온 것의 시작시간으로 점프
        else:
            times = jobs[idx][0]

            
        
    answer = avg_sum // cnt
    return answer