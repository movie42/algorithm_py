# 백준 온라인 저지 단계별 문제풀이 8단계 기본 수학1
# https://www.acmicpc.net/step/8
# 2292
# https://www.acmicpc.net/problem/2292

n = int(input())

now = 1

for i in range(10000000001):
    now += 6 * i
    if now >= n:
        print(i + 1)
        break
