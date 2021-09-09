# 백준 온라인 저지 단계별 문제풀이 if문 2단계
# https://www.acmicpc.net/step/4
# 1330
# https://www.acmicpc.net/problem/1330

a = list(map(int, input().split(' ')))

num1 = a[0]
num2 = a[1]

if num1 > num2:
    print(">")
elif num1 < num2:
    print("<")
elif num1 == num2:
    print("==")