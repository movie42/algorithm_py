# 단계별 문제 1단계 입출력과 사칙연산
# https://www.acmicpc.net/step/1
# 1001번
# https://www.acmicpc.net/problem/1001


a = list(map(int, input().split(' ')))

subtract = 0

for i in range(len(a)):
    if(subtract == 0):
        subtract = a[i]
    else:
        subtract -= a[i]

print(subtract)