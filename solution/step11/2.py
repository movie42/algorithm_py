# 백준 온라인 저지 단계별 문제풀이 10단계 브루트 포스
# https://www.acmicpc.net/step/22
# 7568
# https://www.acmicpc.net/problem/7568

N = int(input())
lst = [0 for i in range(N)]
people = []

for i in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

for i in range(N):
    for j in range(i+1, N):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            lst[j] += 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            lst[i] += 1

for i in lst:
    print(i+1, end=" ")
