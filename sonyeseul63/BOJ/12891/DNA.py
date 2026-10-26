n, m = map(int, input().split())
dna = input().strip()
check = list(map(int, input().split()))

cntArr = [0] * 4
mapping = {'A':0, 'C':1, 'G':2, 'T':3}
count = 0

# 첫 부분 문자열
for ch in dna[:m]:
    idx = mapping[ch]
    cntArr[idx] += 1

# 검사
def ok():
    for i in range(4):
        if cntArr[i] < check[i]:
            return False 
    return True

if ok(): count += 1

# 다음 부분 문자열 & 검사
for idx in range(m, n):
    l = idx - m
    cntArr[mapping[dna[l]]] -= 1
    cntArr[mapping[dna[idx]]] += 1

    if ok(): count += 1

print(count)