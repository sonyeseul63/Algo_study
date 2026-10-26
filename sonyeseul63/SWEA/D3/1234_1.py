T = 1
for test_case in range(1, T+1):
    n, password = input().split()
    
    st = []
    for n in password:
        if st and st[-1] == n:
            st.pop()
        else:
            st.append(n)
    s = "".join(map(str, st))
    print(f"#{test_case} {s}")