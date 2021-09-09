# 백준 온라인 저지 단계별 문제풀이 for문 3단계
# https://www.acmicpc.net/step/3
# 10950
# https://www.acmicpc.net/problem/10950

n = int(input())

sum = 0

for i in range(n):
    array = list(map(int, input().split(' ')))
    if sum == 0:
        sum = array[0]
    sum += array[1]
    print(sum)
    sum = 0
