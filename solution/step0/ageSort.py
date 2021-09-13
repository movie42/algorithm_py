#
#
# 10814
# https://www.acmicpc.net/problem/10814

n = int(input())

array = []

for i in range(n):
    m = input().split(' ')
    array.append((int(m[0]), m[1]))

array = sorted(array, key=lambda x: x[0])

for i in array:
    print(i[0], i[1])
