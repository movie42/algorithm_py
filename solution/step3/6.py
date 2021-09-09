# 백준 온라인 저지 단계별 문제풀이 for문 3단계
# https://www.acmicpc.net/step/3
# 11022
# https://www.acmicpc.net/problem/11022

n = int(input())

for i in range(n):
    a, b = map(int, input().split(' '))
    print("Case #%d: %d + %d = %d" % (i+1, a, b, a+b), end='\n')
