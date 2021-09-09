# 백준 온라인 저지 단계별 문제풀이 5단계 1차원 배열
# https://www.acmicpc.net/step/6
# 1546
# https://www.acmicpc.net/problem/1546

n = int(input())
array = list(map(int, input().split(' ')))

max = float("-inf")
for i in array:
    if max < i:
        max = i

newCount = [(x/max)*100 for x in array]

average = 0
for i in newCount:
    average += i

average = average/n

print(average)
