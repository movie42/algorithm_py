# 백준 온라인 저지 단계별 문제풀이 10단계 브루트 포스
# https://www.acmicpc.net/step/22
# 2798
# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max = 0
sum = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum += cards[i]+cards[j]+cards[k]
            if max < sum and sum <= M:
                max = sum
                sum = 0
            else:
                sum = 0

print(max)
