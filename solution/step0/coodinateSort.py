#
#
# 10814
# https://www.acmicpc.net/problem/10814

n = int(input())

array = []

for i in range(n):
    x, y = map(int, input().split(' '))
    array.append((x, y))

array = sorted(array)

for i in array:
    print(i[0], i[1])
