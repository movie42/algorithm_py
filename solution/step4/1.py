# 백준 온라인 저지 단계별 문제풀이 while문 4단계
# https://www.acmicpc.net/step/2
# 10951
# https://www.acmicpc.net/problem/10951

import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().strip().split(' '))
        print(a + b)
    except:
        break