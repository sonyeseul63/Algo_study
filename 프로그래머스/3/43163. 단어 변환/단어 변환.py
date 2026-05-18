from collections import deque
def solution(begin, target, words):
    answer = 0
    def bfs():
        dq = deque()
        dq.append((begin, 0))
        visited = [] # 방문 목록
        while dq:
            cur, cnt = dq.popleft()
            
            if cur == target:
                return cnt
            
            # 다음거 탐색
            for word in words:
                if not word in visited:
                    # 단어에서 알파벳 하나만 바꾸기 -> 다른 거 하나
                    isOne = 0
                    for i in range(len(cur)):
                        if cur[i] != word[i]:
                            isOne += 1
                    if isOne == 1:
                        dq.append((word, cnt + 1))
                        print(dq)
                        visited.append(word)

    
    if target in words:
        answer = bfs()

    return answer