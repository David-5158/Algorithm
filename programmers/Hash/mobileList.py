def solution(phoneBook):
    # sorted가 중요 순서대로 정렬한 순간부터 차례대로 비교만 하면됨
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):

        if p2.startswith(p1):
            return False
    return True
print(solution(["6", "12", "6789"]))


# def solution(phone_book):
#     # 1. Hash map을 만든다
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
    
#     # 2. 접두어가 Hash map에 존재하는지 찾는다
#     for phone_number in phone_book:
#         jubdoo = ""
#         for number in phone_number:
#             jubdoo += number
#             # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
#             if jubdoo in hash_map and jubdoo != phone_number:
#                 return False
#     return True

# print(solution(["6", "12", "6789"]))



# #이해덜 됨

# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         if len(phone_book[i]) < len(phone_book[i+1]):
#             if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
#                 answer = False
#                 break
#     return answer


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