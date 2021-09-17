#
#
# 17224
# https://www.acmicpc.net/problem/17224
# N:걸그룹수, M:맞춰야할 문제수

N, M = map(int, input().split())
team = {}

for _ in range(N):
    teamName = input()
    team[teamName] = []
    number = int(input())
    for _ in range(number):
        team[teamName].append(input())

for _ in range(M):
    quize = input()
    quizeSort = int(input())
    if quizeSort == 1:
        for key in team:
            if quize in team[key]:
                print(key)
    elif quizeSort == 0:
        for key, item in team.items():
            if quize == key:
                item.sort()
                for i in item:
                    print(i)
