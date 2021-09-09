# 백준 온라인 저지 단계별 문제풀이 2단계
# https://www.acmicpc.net/step/4
# 2884
# https://www.acmicpc.net/problem/2884

a = list(map(int, input().split(' ')))
result = []

if a[0] == 0:
    num = 24*60
else:
    num = a[0]*60
num2 = a[1]

num3 = num + num2
num3 -= 45

if num3//60 == 24:
    result.append("0")
else:
    result.append(str(num3//60))

result.append(str(num3 % 60))

c = ' '.join(result)
print(c)