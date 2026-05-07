from collections import deque
T = 10

def bfs(start, end):
    dq = deque()
    dq.append(start)

    # 큐 순회
    dr = (-1,1,0,0)
    dc = (0,0,-1,1)
    while(dq):
        r, c = dq.popleft()
        if (r, c) == end:
            return 1
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc > n:
                continue
            if maze[nr][nc] == 1:
                continue
            if visited[nr][nc] > 0:
                continue
            visited[nr][nc] = 1
            dq.append((nr, nc))
    
    return 0



for test_case in range(1, T+1):
    case_num = int(input())

    # 미로 입력받기
    n = 16
    maze = []
    for i in range(n):
        line = list(map(int, input()))
        for j, value in enumerate(line):
            if value == 2:
                start = (i, j)
            elif value == 3:
                end = (i, j)
        maze.append(line)
    visited = [[0] * n for _ in range(n)]
    
    res = bfs(start, end)
    print(f"#{case_num} {res}")