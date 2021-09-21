# 백준 온라인 저지 단계별 문제풀이 10단계 기본 수학1
# https://www.acmicpc.net/step/22
# 2231
# https://www.acmicpc.net/problem/2231

number = int(input())
solution = 0
for i in range(1, number+1):
    arr = list(map(int, str(i)))
    solution = i + sum(arr)

    if solution == number:
        print(i)
        break

    if i == number:
        print(0)
