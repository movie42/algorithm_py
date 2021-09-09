# 백준 온라인 저지 단계별 문제풀이 for문 3단계
# https://www.acmicpc.net/step/3
# 15552
# https://www.acmicpc.net/problem/15552

import sys

n = int(sys.stdin.readline().strip())


for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    print(a+b)