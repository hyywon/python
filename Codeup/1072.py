
# 문제
# n개의 정수가 순서대로 입력된다.
# -2147483648 ~ +2147483647, 단 n의 최대 개수는 알 수 없다.
# n개의 입력된 정수를 순서대로 출력해보자.

# 입력
# 첫 줄에 정수의 개수 n이 입력되고,
# 두 번째 줄에 n개의 정수가 공백을 두고 입력된다.
# -2147483648 ~ +2147483647, 단 n의 최대 개수는 알 수 없다.

# 출력
# n개의 정수를 한 개씩 줄을 바꿔 출력한다.

A = input()
A = int(A)
num = []
num = input().split()

for i in range(0,A):
    print(num[i])
