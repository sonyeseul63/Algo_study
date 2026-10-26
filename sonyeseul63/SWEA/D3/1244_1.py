# 교환 -> 리스트 인덱스 이용, 합칠때는 join
# 1번 -> 두 숫자 자리 바꾸기, 원본을
# n번 -> 반복, 회차 바꿔질때마다 바뀐 숫자배열마다
# 두 숫자 자리 바꿔서 목록 생성, 마지막에 그 중 최대 반환
# 교환후 중복된 것 처리 -> set / visited

# bfs + set 
def create_bfs(origin, n):
    # 탐색할 숫자 문자열 목록: 큐가 아니고 set -> 최소/최단이 아님, 중복 제거
    origin_num = {origin}
    for _ in range(n):
        after_num = set()
        for now_num in origin_num: 
            # 숫자문자열의 목록 생성(조합)
            for i in range(len(now_num)-1):
                for j in range(i+ 1, len(now_num)): 
                    arr = list(now_num)
                    arr[i], arr[j] = arr[j], arr[i]
                    after_num.add(''.join(arr))
        origin_num = after_num
    return max(after_num)

# 재귀 -> 비교대상(max) 전역으로 관리
def create_dfs1(s, depth):
    global answer
    if depth == n:
        answer = max(s, answer)
        return

    # 다음 숫자문자열 생성
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            arr = list(s)
            arr[i], arr[j] = arr[j], arr[i]
            value = (''.join(arr), depth +1)
            if value in visited:
                continue
            else:
                visited.add(value)
                create_dfs1(''.join(arr), depth +1)

# 재귀 -> 반환 
def create_dfs2(s, depth):
    if depth == n:
        return s
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            arr = list(s)
            arr[i], arr[j] = arr[j], arr[i]
            next_s = ''.join(arr)
            if (next_s, depth+1) in visited:
                continue
            visited.add((next_s,depth+1))
            value = create_dfs2(next_s, depth+1)
            best = max(best, value)
    return best


T = int(input())
for C in range(1, T+1):
    origin, n = input().split()
    n = int(n)
#   price = create_bfs(origin, n)
#   print(f"#{C} {price})
    visited = set()
    answer = "0"
    create_dfs1(origin, 0)
    print(f"#{C} {answer}")