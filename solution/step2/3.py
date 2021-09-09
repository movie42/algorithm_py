# 백준 온라인 저지 단계별 문제풀이 2단계
# https://www.acmicpc.net/step/4
# 14681
# https://www.acmicpc.net/problem/14681

a = int(input())
b = int(input())

def graph(num1, num2):
    if a > 0:
        if b > 0:
            return 1
        elif b < 0:
            return 4
    elif a < 0:
        if b > 0:
            return 2
        elif b < 0:
            return 3

print(graph(a,b))