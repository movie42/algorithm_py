#
#
# 10989
# https://www.acmicpc.net/problem/10989

import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    m = int(sys.stdin.readline())
    array[m] += 1

for i in range(len(array)):
    if i != 0:
        for j in range(array[i]):
            print(i)
