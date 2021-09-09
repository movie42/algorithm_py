# 백준 온라인 저지 단계별 문제풀이 while문 4단계
# https://www.acmicpc.net/step/2
# 1110
# https://www.acmicpc.net/problem/1110

n = input()
m = int(n)

count = 1
while True:
    if m < 10:
        m = "0"+str(m)
    else:
        m = str(m)
    a = int(m[:1]) + int(m[1:])
    if a < 10:
        b = "0" + str(a)
    else:
        b = str(a)
    c = m[1:] + b[1:]
    if int(c) == int(n):
        print(count)
        break
    else:
        m = int(c)
        count += 1
