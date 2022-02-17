n = 5
lost = [2,5]
reserve = [1,3,5]
reserve_uniq = set(reserve) - set(lost)
lost_uniq = set(lost) - set(reserve)

# set 함수는 집합이라고 생각하면된당
# 중복제거와 교집합, 합집합, 차집합, 대칭 차집합과 같은 수학 연산을 계산
# 인덱싱, 슬라이싱 등 시퀀스 유사동작 지원 x


print(type(reserve_uniq), lost_uniq)

for i in reserve_uniq :
    if i-1 in lost_uniq :   # set 함수 문법 x in s  = s가 x안에있는지 검사
        lost_uniq.remove(i-1)
    elif i+1 in lost_uniq :
        lost_uniq.remove(i+1)
    
print(n - len(lost_uniq))

