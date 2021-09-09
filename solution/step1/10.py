# 단계별 문제 1단계 입출력과 사칙연산
# https://www.acmicpc.net/step/1
# 2588
# https://www.acmicpc.net/problem/2588

a = int(input())
b = int(input())
bList = [int(i) for i in str(b)]
result = []

for i in range(len(bList)):
    multi = a*bList[i]
    result.append(multi)

for i in range(len(result)):
    print(result.pop())

print(a*b)
            