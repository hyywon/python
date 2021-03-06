# 문제
# 두 단어 A와 B가 주어졌을 때, A에 속하는 알파벳의 순서를 바꾸어서 B를 만들 수 있다면, A와 B를 애너그램이라고 한다.

# 두 단어가 애너그램인지 아닌지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수(<100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 100을 넘지 않는 단어가 공백으로 구분되어서 주어진다. 단어는 알파벳 소문자로만 이루어져 있다.

# 출력
# 각 테스트 케이스마다 애너그램인지 아닌지를 예체 출력과 같은 형식으로 출력한다. 

import sys
read = sys.stdin.readline

anagram = []

N = int(read())

for _ in range(N):
    word = []
    word = read().split()
    anagram.append(word)


for i in range(N):
    A, B = anagram[i]
    # 문자열을 정렬해서 정확하게 같으면 애너그램
    a = sorted(A)
    b = sorted(B)

    if a == b : 
        print("{} & {} are anagrams.".format(A,B))
    else: 
        print("{} & {} are NOT anagrams.".format(A,B))

