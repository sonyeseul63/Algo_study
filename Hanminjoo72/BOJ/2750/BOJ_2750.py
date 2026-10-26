N = int(input())
num = []

for i in range(N):
    num.append(int(input()))
ns = sorted(num)

for i in range(N):
    print(ns[i])