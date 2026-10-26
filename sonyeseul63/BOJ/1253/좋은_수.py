n = int(input())
arr = list(map(int, input().split()))
arr.sort()
count = 0

for idx, num in enumerate(arr):
    i = 0
    j = n - 1
    while (i < j):
        if (i == idx):
            i += 1
            continue
        if(j == idx):
            j -= 1
            continue

        sum = arr[i] + arr[j]

        if(sum < num):
            i += 1
        elif(sum > num):
            j -= 1
        else:
            count += 1
            break

print(count)