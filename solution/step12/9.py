# 백준 온라인 저지 단계별 문제풀이 12단계 정렬
# https://www.acmicpc.net/step/9
# 18870
# https://www.acmicpc.net/problem/18870

import sys

N = int(sys.stdin.readline())
users = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    users.append((age, name))

sorted_users = sorted(users, key=lambda item:int(item[0]))

for i in sorted_users:
    print(i[0], i[1])

