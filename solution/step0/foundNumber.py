#
#
# 1920
# https://www.acmicpc.net/problem/1920

N, Narray, M, Marray = int(input()), list(map(int, input().split())), int(
    input()), list(map(int, input().split()))

for i in Marray:
    if i in Narray:
        print(1)
    else:
        print(0)
