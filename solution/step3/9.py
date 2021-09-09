# 백준 온라인 저지 단계별 문제풀이 for문 3단계
# https://www.acmicpc.net/step/3
# 2439
# https://www.acmicpc.net/problem/2439

n = int(input())

for i in range(1, n+1):
    star = "*" * i
    empty = " " * (n - i)
    print(empty+star)

