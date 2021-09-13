# 백준 온라인 저지 단계별 문제풀이 8단계 기본 수학1
# https://www.acmicpc.net/step/8
# 1712
# https://www.acmicpc.net/problem/1712

import sys
A, B, C = map(int, sys.stdin.readline().split(' '))
# A 생산 대수와 관계없는 고정비용 
# B 한대 생산 가변비용
# C 책정된 가격 

if B >= C:
    print(-1)
else:
    breakEvenPoint = A // (C - B)
    cost = 0
    while True:
        breakEvenPoint += 1
        cost = A + (B * breakEvenPoint)
        if cost < C * breakEvenPoint:
            print(breakEvenPoint)
            break