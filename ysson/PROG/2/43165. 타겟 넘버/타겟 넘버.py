def solution(numbers, target):
    answer = 0
    def dfs(depth, total):
        if depth == len(numbers):
            if total == target:
                return 1
            return 0

        plus = dfs(depth + 1, total + numbers[depth])
        minus = dfs(depth + 1, total - numbers[depth])
    
        return plus + minus
    answer = dfs(0, 0)
    return answer