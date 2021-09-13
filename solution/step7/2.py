# 백준 온라인 저지 단계별 문제풀이 7단계 문자열
# https://www.acmicpc.net/step/7
# 10809
# https://www.acmicpc.net/problem/10809

n = input()
str = [chr(x) for x in range(97, 123)]
index = []

for i in str:
    if i in n:
        index.append(n.index(i))
    else:
        index.append(-1)

for i in index:
    print(i, end=" ")
