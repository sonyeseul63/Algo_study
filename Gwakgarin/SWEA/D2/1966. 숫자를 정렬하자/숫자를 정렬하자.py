T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    #arr.sort() 
    for j in range(N-1):
        mn = j 
        for k in range(j+1, N):
            if arr[k] < arr[mn] :
                mn = k 
        arr[j], arr[mn] = arr[mn], arr[j] 
        
    print(f"#{i+1}", *arr)
    