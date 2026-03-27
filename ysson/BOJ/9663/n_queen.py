N = int(input())
visited = [0] * N # 이미 배치한 열인지
diff_sum = set() # 우하향 대각선
diff = set() # 우상향 대각선
cnt = 0

def bt(row): #dept = row 
    global cnt
    if row == N:
        cnt+=1
        return
    for col in range(N): # 해당 행의 열 정하기
        # 조건: 이미 배치한 열 안됨, 대각선에 배치 안됨
        if not visited[col] and (row-col) not in diff and (row+col) not in diff_sum: 
            visited[col] = 1
            diff_sum.add(row+col)
            diff.add(row-col)
            bt(row+1) # 다음 행
            visited[col] = 0
            diff_sum.discard(row+col)
            diff.discard(row-col)
bt(0)
print(cnt)