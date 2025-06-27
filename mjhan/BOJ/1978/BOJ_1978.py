n = int(input())
number = list(map(int,input().split()))
sosu = 0

for num in number:
    if num == 1:
        continue
    for x in range(2,num):
        if(num % x == 0):
            break
    else:
        sosu += 1
print(sosu)