from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        # 첫번째단어 and 두번째단어 
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
            print(str1_lst)
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
            print(str2_lst)

    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    print(Counter1)
    print(Counter2)


    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    print(inter)
    print(union)

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
    
print(solution("handshake","shake hands"))