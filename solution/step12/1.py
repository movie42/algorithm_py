# 백준 온라인 저지 단계별 문제풀이 12단계 정렬
# https://www.acmicpc.net/step/9
# 2751
# https://www.acmicpc.net/problem/2751

import sys
N = int(sys.stdin.readline())
data_list = list()
for i in range(N):
    data_list.append(sys.stdin.readline())

sort_list = sorted(data_list)

for i in sort_list:
    print(i)
