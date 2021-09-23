# 백준 온라인 저지 단계별 문제풀이 10단계 재귀
# https://www.acmicpc.net/step/19
# 10870
# https://www.acmicpc.net/problem/10870

n = int(input())


def fibonacii(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacii(num-1)+fibonacii(num-2)


print(fibonacii(n))
