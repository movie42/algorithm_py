# 과제
# 이어붙인 수중 가장 큰 수를 만들기

import itertools


array = list(input().split())


def isMax(arr):
    max = 0
    permutationArray = list(map(''.join, itertools.permutations(arr)))
    for i in permutationArray:
        if int(i) > max:
            max = int(i)
    return int(max)


print(isMax(array))
