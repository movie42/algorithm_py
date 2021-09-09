# 백준 온라인 저지 단계별 문제풀이 2단계
# https://www.acmicpc.net/step/4
# 2753
# https://www.acmicpc.net/problem/2753

a = int(input())

def fourYear(year):
    if a%4 ==0 and a%100 != 0 or a%400 == 0:
        return 1
    else:
        return 0

print(fourYear(a))