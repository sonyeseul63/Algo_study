N = int(input())

def isPrime(n):
    if n == 2: return True
    for i in range(2, n):
        if(n % i == 0):
            return False
    else: return True

def dfs(x, len):
        if(len == N):
            print(x)
            return
        
        for i in [1,3,7,9]:
            next = 10 * x + i
            if isPrime(next):
                dfs(next, len+1)

for n in [2,3,5,7]:
    dfs(n, 1)