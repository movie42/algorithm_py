# 백준 온라인 저지 단계별 문제풀이 10단계 기본 수학1
# https://www.acmicpc.net/step/19
# 2447
# https://www.acmicpc.net/problem/2447

n = int(input())


def starts(num):
    for i in range(1, num*num+1):
        if i % 3 == 0:
            return "*\n"
        elif i == num*num // 2 + 1:
            return " "
        else:
            return "*"


print(starts(n))
