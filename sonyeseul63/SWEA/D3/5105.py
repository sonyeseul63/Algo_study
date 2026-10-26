from collections import deque
T = int(input())

# start(set 타입)에서 시작해서 3까지 좌표 개수 구하기
def bfs(start, end):
    dq = deque()
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    # 초기값 큐에 넣기
    dq.append(start)
    
    # 큐에서 값 꺼내어 주변 좌표 순회
    while(dq):
        (cr, cc) = dq.popleft()

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # 다음 좌표 범위 검사
            if 0<=nr<n and 0<=nc<n:
                # 종료 조건
                if (nr, nc) == end:
                    return arr[cr][cc] -2
                # 후보 조건
                if arr[nr][nc] == 0:
                    arr[nr][nc] = arr[cr][cc] + 1
                    dq.append((nr, nc))
    
    return 0

for test_case in range(1, T+1):
    n = int(input())
    # 미로 입력 + 출발점 탐색: 완탐인데 숫자가 크지 않아서 ㄱㅊ
    arr = []
    for i in range(n):
        row = (list(map(int, input())))
        for j, value in enumerate(row):
            if value == 2:
                start = (i, j)
            if value == 3:
                end = (i, j)
        arr.append(row)

    result = bfs(start, end)
    print(f"#{test_case} {result}")