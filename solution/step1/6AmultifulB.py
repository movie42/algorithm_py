# 단계별 문제 1단계 입출력과 사칙연산
# https://www.acmicpc.net/step/1
# 10998번
# https://www.acmicpc.net/problem/10998

a = list(map(int, input().split(' ')))

multiple = 1

for i in a:
    multiple *= i

print(multiple)