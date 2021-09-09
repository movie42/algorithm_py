# 백준 온라인 저지 단계별 문제풀이 5단계 1차원 배열
# https://www.acmicpc.net/step/6
# 3052
# https://www.acmicpc.net/problem/3052 

list = []
for i in range(10):
    n = int(input())
    m = n % 42
    list.append(m)

list.sort()

i = 0
j = 1
count = 1
while j < len(list):
    if list[i] == list[j]:
        j += 1
    else:
        count += 1
        i = j
        j += 1

print(count)