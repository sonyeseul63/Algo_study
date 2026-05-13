T = 10
for test_case in range(1, T+1):
    n = int(input())
    heights = list(map(int, input().split()))
    for _ in range(n):
        max_i = heights.index(max(heights))
        min_i = heights.index(min(heights))
        heights[max_i]-=1
        heights[min_i]+=1
        max_i = heights.index(max(heights))
        min_i = heights.index(min(heights)) 
        gap = heights[max_i]- heights[min_i]
        if gap <= 1:
            break
    print(f"#{test_case} {gap}")
