def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

#이해덜 됨
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer


# phoneBook = ["119", "97674223", "1195524421"]
# phoneBook = sorted(phoneBook)
# print(phoneBook)
# cnt = 0
# print(list(zip(phoneBook, phoneBook[1:])))
# for p1, p2 in zip(phoneBook, phoneBook[1:]):
#     cnt +=1
#     print(cnt,p1,p2)
#     if p2.startswith(p1):
#         print(False)
#     else:
#         print(True)