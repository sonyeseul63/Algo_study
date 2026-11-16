T = int(input())
for i in range(T):
    N = int(input())
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * 8 
    
    for j in range(8):
        cnt[j] = N//arr[j]
        N = N%arr[j]
        
    print(f"#{i+1}")
    print(*cnt)
          
        