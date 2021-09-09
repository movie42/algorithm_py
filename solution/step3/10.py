# 백준 온라인 저지 단계별 문제풀이 for문 3단계
# https://www.acmicpc.net/step/3
# 10871
# https://www.acmicpc.net/problem/10871

import sys

a, b = map(int, sys.stdin.readline().strip().split(' '))
array = list(map(int, sys.stdin.readline().strip().split(' ')))

for i in range(a):
    if array[i] < b:
        print(array[i], end=" ")
