# 백준 온라인 저지 단계별 문제풀이 if문 2단계
# https://www.acmicpc.net/step/4
# 9498
# https://www.acmicpc.net/problem/9498

a = int(input())

if a>=90 and a<=100:
    print("A")
elif a>=80 and a<=89:
    print("B")
elif a>=70 and a<=79:
    print("C")
elif a>=60 and a<=69:
    print("D")
else:
    print("F")