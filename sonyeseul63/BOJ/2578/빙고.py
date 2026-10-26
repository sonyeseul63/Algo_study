d = dict()
for i in range(5):
    l = list(map(int, input().split()))
    for j, k in enumerate(l):
        d[k] = (i, j)
board = []
for i in range(5):
    l = list(map(int, input().split()))
    board.append(l)

def solve():
    row = [0] * 5
    col = [0] * 5
    diag1 = 0 # 우하향
    diag2 = 0 # 우상향
    cnt = 0
    num = 0
    for i in range(5):
        for k in board[i]:
            num += 1
            (i, j) = d[k]
            row[i] += 1
            col[j] += 1
            if row[i] == 5:
                cnt += 1
            if col[j] == 5:
                cnt += 1
            if i == j: 
                diag1 += 1
                if diag1 == 5:
                    cnt += 1
            if i+j == 4: 
                diag2 += 1
                if diag2 == 5:
                    cnt += 1
            if cnt >= 3: return num

print(solve())