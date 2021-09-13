# 백준 온라인 저지 단계별 문제풀이 5단계 1차원 배열
# https://www.acmicpc.net/step/6
# 4344
# https://www.acmicpc.net/problem/4344

n = int(input())

average = 0
count = 0
for _ in range(n):
    array = list(map(int, input().split(" ")))
    average = 0
    count = 0
    for i in array[1:]:
        average += i

    average = average/array[0]

    for i in array[1:]:
        if i > average:
            count += 1

    percent = (count/array[0])*100
    print('%.3f%s' % (percent, "%"))
