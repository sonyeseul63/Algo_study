n, m = map(int, input().split())

permutation = []
visited = [0] * (n+1)

def bt(depth):
    if depth == m:
        print(*permutation)
        return # 자리수가 차면 되돌아가기
    
    # 숫자 순회(순열 만들기)
    for next in range(1, n+1):
        if visited[next] == 0: # 다음 숫자의 조건
            permutation.append(next)
            visited[next] = 1
            # 다음 숫자 재귀
            bt(depth + 1)
            # 돌아온 후에 visited 해제, 순열에서 제거
            visited[next] = 0
            permutation.pop()

bt(0)