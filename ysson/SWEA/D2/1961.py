T=int(input())
def rotated(board):
    rotated = [ [] for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            rotated[i].append(board[n-j-1][i])
    return rotated

for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = [ [] for _ in range(n) ]
    # 3번 회전
    for i in range(3):
        board = rotated(board)
        # 회전 후의 배열 한 row를 합쳐서 한 원소로
        for j in range(n):
            row = ''.join(map(str, board[j]))
            res[j].append(row)
    # 출력
    print(f"#{test_case}")
    for i in range(n):
        print(*res[i])
        