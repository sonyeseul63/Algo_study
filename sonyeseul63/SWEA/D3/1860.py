# 목표: N개
# M초 당 K개
# N, M. K -> N개, M당 K개
# 손님 마다 언제 오는지
# 출력: 손님들 모두에게 붕어빵 바로 줄 수 있나 (검증)

T = int(input())
for test_case in range(1, T+1):
    n, m, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()



    # 사람수, 도착 시간, 기준을 어떤걸로                                잡고 for? -> 판단이 일어나는 순간
    # 시간에 따라 상태가 복잡하게 변함 -> 시뮬레이션, 깜끔히 떨어지지않음.. 경계값이
    # 시간에 따라 만들어지는 상태가 단순하고 일반적 -> 일반 수식
    # 손님이 오는 시점에만 붕어빵 여부
    # 매번 새로운 구간을 검증하기에는 이전 사람과 현재 사람사이에 만들어진 붕어빵을 일일이 계산하기에 굳이?
    # 그떄 그때 검증한다면 누적량을 해도 무방하다
    made = 0
    impo = False
    for i in range(n): # 한명씩
        target = p[i]

        # 이전 m의 배수까지만큼 붕어빵을 만듬, target과 현재시간 차이가 m이면..
        made = ((target) // m ) * k
        
        # 총 수요까지 양이 ㄱㅊ은가? 
        if made< 1+i:
            impo = True
            break
        made -= 1
        
    
    if impo:
        print(f"#{test_case} Impossible")
    else:
        print(f"#{test_case} Possible")
