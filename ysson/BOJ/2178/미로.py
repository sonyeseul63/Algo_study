from collections import deque

N, M = map(int, input().split())
miro = [ list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [ [0] * M for _ in range(N) ]

def bfs(x, y):
    queue = deque()

    # 시작점
    queue.append((x,y))
    visited[x][y] = 1

    # 현재의 좌표
    while(queue):
        x, y = queue.popleft()

        # 다음 좌표
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and miro[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    if visited[N-1][M-1] > 0:
                        return
                    queue.append((nx,ny))
    
bfs(0, 0)
print(visited[N-1][M-1])