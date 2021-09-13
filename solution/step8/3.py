# 백준 온라인 저지 단계별 문제풀이 8단계 기본 수학1
# https://www.acmicpc.net/step/8
# 1193
# https://www.acmicpc.net/problem/1193

n = int(input())

now = 0
for i in range(1, 10000001):
    now += i
    if now >= n:
        if i % 2 == 0:
            print('%d/%d' % ((i - (now - n)), (1 + (now - n))))
            break
        else:
            print('%d/%d' % ((1 + (now - n)), (i - (now - n))))
            break


