#
# 다시풀어보기
# 17224
# https://www.acmicpc.net/problem/17224
# N:문제 개수 L:현정이의 역량 K:현정이가 대회때 풀수 있는 문제의 수

N, L, K = map(int, input().split())

score = 0
easy, hard = 0, 0
for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1
score = min(hard, K) * 140

if hard < K:
    score += min(K-hard, easy) * 100

print(score)
