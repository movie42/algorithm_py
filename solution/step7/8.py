# 백준 온라인 저지 단계별 문제풀이 7단계 문자열
# https://www.acmicpc.net/step/7
# 1316
# https://www.acmicpc.net/problem/1316

n = int(input())

i = 0
j = 1
count = n

for i in range(n):
    checker = []    
    str = input()
    i = 0
    j = 1
    while j < len(str):
        if str[j] in checker:
            count -= 1
            break
        if str[i] != str[j]:
            checker.append(str[i])
            i = j
            j += 1
        else:
            j += 1
            

print(count)
        



