n = int(input())
white = [[0]*101 for _ in range(101)] #도화지
width = 0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
       for j in range(y, y+10):
           if white[i][j]==0:
               white[i][j]=1
               width+=1
print(width)