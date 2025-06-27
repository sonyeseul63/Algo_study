x = int(input())
n = int(input())
sum = 0
for i in range(n):
    price , count = map(int,input().split())
    sum += (price * count)

if x == sum:
    print("Yes")
else:
    print("No")