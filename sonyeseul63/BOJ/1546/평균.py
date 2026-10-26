n = int(input())
score = list(map(int,input().split()))
maxNum = max(score)
print(sum(score) / n * 100 / maxNum) 
