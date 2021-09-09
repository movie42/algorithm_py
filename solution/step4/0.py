# 백준 온라인 저지 단계별 문제풀이 while문 4단계
# https://www.acmicpc.net/step/2
# 10952
# https://www.acmicpc.net/problem/10952

import sys

while True:
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    if a == 0 and b == 0:
        break
    print(a + b)