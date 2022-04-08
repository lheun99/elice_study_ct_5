def solution(phone_book):
    phone_book.sort()
    # print(phone_book)
    # try:
    for idx in range(len(phone_book)):
        if phone_book[idx+1].startswith(phone_book[idx]):
            return False
    return True
    # except IndexError:
    #     return True


print(solution(["12", "123", "1235", "567", "88"]))
