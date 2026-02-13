n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

i = 0
j = n-1
count = 0
while i < j:
    sum = arr[i] + arr[j]
    if(sum > m):
        j -= 1
    elif(sum < m):
        i += 1
    else:
        count += 1
        j -= 1
        i += 1

print(count)