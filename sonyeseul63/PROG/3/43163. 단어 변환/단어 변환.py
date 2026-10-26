from collections import deque
def solution(begin, target, words):
    answer = 0
    dq = deque()
    
    def isOne(word, cur):
        cnt = 0
        for i in range(len(cur)):
            if word[i] != cur[i]:
                cnt += 1
            
        if cnt == 1:
            return True
        else:
            return False
    
    
    def bfs():
        res = 0
        dq.append((begin, 0))
        visited = []
        while dq:
            cur, depth = dq.pop()
        
            if cur == target:
                res = depth
                break
            
            for word in words:
                if word not in visited:
                    if isOne(word, cur):
                        dq.append((word, depth+1))
                        visited.append(word)
        return res
                              
    answer = bfs()
        
    return answer