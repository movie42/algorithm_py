# 백준 온라인 저지 단계별 문제풀이 8단계 기본 수학1
# https://www.acmicpc.net/step/8
# 10250
# https://www.acmicpc.net/problem/10250


j = int(input())

for i in range(j):
    h, w, n = map(int, input().split(' '))
    a = n % h
    b = n//h + 1
    if a == 0:
        a = h 
        b = n//h
    print(f'{a*100+b}')