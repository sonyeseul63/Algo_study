N, M = map(int, input().split())

visited = [0] * (N+1)
# arr를 만들어서 수열이 만들어질때마다 print할 것
arr = []
length = 0

# 한 수열 만드는 함수
def f(length):
    if(length == M): 
        print(*arr)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            arr.append(i)
            f(i, length+1)
            arr.pop()
            visited[i] = 0
            

f(0)