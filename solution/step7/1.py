# 백준 온라인 저지 단계별 문제풀이 7단계 문자열
# https://www.acmicpc.net/step/7
# 11720
# https://www.acmicpc.net/problem/11720

n = int(input())
array = list(map(int, list(input())))
sum = 0
for i in array:
    sum += i

print(sum)
