T = int(input())
for i in range(T): 
    N = int(input())
    arr = [2, 3, 5, 7, 11]
    cnt = [0] * 5 
    
    for j in range(5):
        while N % arr[j] ==0 : 
            cnt[j] +=1 
            N = N//arr[j]
    
    print(f"#{i+1}", *cnt)