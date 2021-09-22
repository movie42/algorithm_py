# 백준 온라인 저지 단계별 문제풀이 12단계 정렬
# https://www.acmicpc.net/step/9
# 10814
# https://www.acmicpc.net/problem/18870

import sys

N = int(sys.stdin.readline())
position = list(map(int, sys.stdin.readline().split()))

compressor = sorted(set(position))

dict = {compressor[i]:i  for i in range(len(compressor))}

for i in position:
    print(dict[i], end=" ")
