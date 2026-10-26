N = int(input())

#이름으로 찾아서 삽입과 삭제가 빠른 자료구조? dict, set
s = set()

for _ in range(N):
    name, state = input().split()
    if state == 'enter':
        s.add(name)
    else:
        s.remove(name)


print(*sorted(s, reverse=True), sep="\n")