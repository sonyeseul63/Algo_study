N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * N for _ in range(N)]
count = 0
arr = []


def dfs(x, y):
    global count
    # 현재 좌표에 대한 처리
    count += 1
    visited[x][y] = 1

    # 다음 좌표
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if board[i][j]==1 and not visited[i][j]:
            dfs(i, j)
            arr.append(count)
            count = 0

arr.sort()
print(len(arr))
print("\n".join(map(str, arr)))