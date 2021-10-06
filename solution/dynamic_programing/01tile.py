# BOJ
# 01타일
# https://www.acmicpc.net/problem/1904


def dp(N):
    d = [0]*1000001
    d[1] = 1
    d[2] = 2
    for i in range(3, N+1):
        d[i] = (d[i-2] + d[i-1]) % 15746
    return d[N]


print(dp(5))
