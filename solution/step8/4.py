# 백준 온라인 저지 단계별 문제풀이 8단계 기본 수학1
# https://www.acmicpc.net/step/8
# 2869
# https://www.acmicpc.net/problem/2869

import math, sys
A, B, V = map(int, input().split(' '))

days = (V-B) / (A-B)
print(math.ceil(days))

sys.stdin.readline()
