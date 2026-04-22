def solution(a, b):
    # 파이썬은 내부적으로 아주 큰 숫자(BigInt)도 자동으로 처리해주기 때문에
    # 문자열을 숫자로 바꿔서 더한 뒤 다시 문자열로만 돌려주면 됩니다.
    return str(int(a) + int(b))