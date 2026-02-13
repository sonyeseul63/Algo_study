n = int(input())

count = 1
sum = 1
i, j = 1, 1

while j < n:
    if sum == n:
        count += 1
        sum -= i
        i += 1
    elif sum < n:
        j += 1
        sum += j
    else:  # sum > n
        sum -= i
        i += 1

print(count)