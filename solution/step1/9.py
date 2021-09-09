# 단계별 문제 1단계 입출력과 사칙연산
# https://www.acmicpc.net/step/1
# 10430
# https://www.acmicpc.net/problem/10430

a = list(map(int, input().split(' ')))
A = a[0]
B = a[1]
C = a[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
            