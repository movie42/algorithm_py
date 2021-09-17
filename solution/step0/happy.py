#
#
# 15969
# https://www.acmicpc.net/problem/15969

n = int(input())
array = list(map(int, input().split(' ')))

minScore = min(array)
maxScore = max(array)

print(maxScore - minScore)
