# 단계별 문제 1단계 입출력과 사칙연산
# https://www.acmicpc.net/step/1
# 10869번
# https://www.acmicpc.net/problem/10869

a = list(map(int, input().split(' ')))

tool = ["+", "-", "*", "/", "%"]
result = 0

for i in range(len(tool)):
    if tool[i] == "+":
        result = a[0] + a[1]
        print(result)
    elif tool[i] == "-":
        result = a[0] - a[1]
        print(result)
    elif tool[i] == "*":
        result = a[0] * a[1]
        print(result)
    elif tool[i] == "/":
        result = a[0] / a[1]
        print(int(result))
    elif tool[i] == "%":
        result = a[0] % a[1]
        print(result)
