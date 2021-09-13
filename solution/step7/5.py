# 백준 온라인 저지 단계별 문제풀이 7단계 문자열
# https://www.acmicpc.net/step/7
# 2908
# https://www.acmicpc.net/problem/2908

n = input().split()

if int(n[0][::-1]) > int(n[1][::-1]):
    print(int(n[0][::-1]))
else:
    print(int(n[1][::-1]))
