
# 문제
# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D로 평가되어야 한다.

# 입력
# 정수(0 ~ 100) 1개가 입력된다.

# 출력
# 평가 결과를 출력한다.

A = input()
A = int(A)

if A>=90:
    print("A")
elif A>=70 and A<=89:
    print("B")
elif A>=40 and A<=69:
    print("C")
else:
    print("D")