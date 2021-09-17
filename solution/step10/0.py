# 백준 온라인 저지 단계별 문제풀이 10단계 기본 수학1
# https://www.acmicpc.net/step/19
# 10872
# https://www.acmicpc.net/problem/10872

n = int(input())


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


print(factorial(n))
