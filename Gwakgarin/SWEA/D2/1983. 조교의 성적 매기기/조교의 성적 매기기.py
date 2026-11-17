T = int(input())
for i in range(T):
    N, k = map(int, input().split())
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"] 
    total = [ ] 
    
    for j in range(N):
        mid, fin, hw = map(int, input().split())
        total.append(mid * 35 + fin * 45 + hw * 20)
        
    target = total[k-1]
    total.sort(reverse=True)
    rank = total.index(target)
    ans = grade[ rank // (N//10) ] 
    
    print(f"#{i+1} {ans}")