# 백준 온라인 저지 단계별 문제풀이 5단계 1차원 배열
# https://www.acmicpc.net/step/6
# 10818
# https://www.acmicpc.net/problem/10818

p = input()
array = list(map(int, input().split(' ')))

array.sort()

print(array[0], array[-1])