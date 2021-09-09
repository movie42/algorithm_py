# 단계별 문제 1단계 입출력과 사칙연산
# https://www.acmicpc.net/step/1
# 1000번
# https://www.acmicpc.net/problem/1000

a = list(map(int, input().split(" ")))

sum = 0
for i in range(len(a)):
    sum += a[i]

print(sum)