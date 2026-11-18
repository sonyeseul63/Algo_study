T = int(input())
for test_case in range(1, T+1):
    word = str(input())
    new_word = word[::-1] 
    ans = 1
    
    if word !=new_word : 
        ans = 0 
   
    print(f"#{test_case} {ans}") 
    