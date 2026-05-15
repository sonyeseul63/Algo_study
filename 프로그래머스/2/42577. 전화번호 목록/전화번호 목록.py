def solution(phone_book):
    answer = True
    phone_hash = set(phone_book)
    for book in phone_book:
        for i in range(1, len(book)):
            if book[:i] in phone_hash:
                answer = False
                break
    return answer