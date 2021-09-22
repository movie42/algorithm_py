# 백준 온라인 저지 단계별 문제풀이 12단계 정렬
# https://www.acmicpc.net/step/9
# 10989
# https://www.acmicpc.net/problem/10989

import sys

N = int(sys.stdin.readline())
count_list = [0]*10001

for i in range(N):
    num = int(sys.stdin.readline())
    count_list[num] += 1

for i in range(len(count_list)):
    if count_list[i] != 0:
        for j in range(count_list[i]):
            print(i)

    

