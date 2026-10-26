n, m = map(int, input().split())
nums = list(map(int, input().split()))

prefixSum = 0
count = [0] * m
count[0] = 1
result = 0

for index, num in enumerate(nums):
    prefixSum = (prefixSum + num) % m
    result += count[prefixSum]
    count[prefixSum] += 1

print(result)
