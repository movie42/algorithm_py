# BOJ
# 01타일
# https://www.acmicpc.net/problem/1904

N = int(input())


def dp(N):
    save_data = [0] * 1000001
    save_data[1] = 1
    save_data[2] = 2

    for i in range(3, N+1):
        save_data[i] = (save_data[i-2] + save_data[i-1]) % 15746
    return save_data[N]


print(dp(N))
