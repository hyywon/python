# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다.
# 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치,
# b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
# 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

word = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

count = [-1] * 26
cnt = 0

for i in word:
    for j in alpha:
        if i == j:
            # 알파벳에 해당하는 ascii 값 97(소문자 a)를 뺌
            # 해당 위치 값이 -1인 경우에만 변경
            if count[ord(j) - 97] == -1:
                count[ord(j) - 97] = cnt
    cnt += 1
        
for i in range(26):
    print(count[i],end=' ')