# 백준 온라인 저지
# https://www.acmicpc.net/problem/2798

# 주어진 카드의 합이 M이거나 
# M에 최대한 가까운 카드 3장의 합을 구하기

N, M = map(int, input().split())
card = list(map(int, input().split()))

max = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i]+card[j]+card[k] > max and card[i]+card[j]+card[k] <= M:
                max = card[i]+card[j]+card[k]
            if max == M:
                break
print(max)


