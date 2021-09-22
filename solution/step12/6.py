# 백준 온라인 저지 단계별 문제풀이 12단계 정렬
# https://www.acmicpc.net/step/9
# 11651
# https://www.acmicpc.net/problem/11651

from operator import itemgetter
N = int(input())
position = []

for i in range(N):
    x, y = map(int, input().split())
    position.append((x, y))

position_sorted = sorted(position, key=itemgetter(0, 1))

for i in position_sorted:
    print(i[0], i[1])