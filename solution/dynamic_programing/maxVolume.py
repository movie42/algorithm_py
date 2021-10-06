# 기타리스트
# https://www.acmicpc.net/problem/1495
# 마지막곡의 최대 볼률 값 구하기

# N, S, M = map(int, input().split())
# V = list(map(int, input().split()))

# volum_list = [[0] * (M+1) for _ in range(N+1)]
# volum_list[0][S] = 1

# for i in range(1, N+1):
#     for j in range(M + 1):
#         if volum_list[i-1][j] == 0:
#             continue
#         if j - V[i-1] >= 0:
#             volum_list[i][j-V[i-1]] = 1
#         if j + V[i-1] <= M:
#             volum_list[i][j+V[i-1]] = 1

# result = -1

# for i in range(M, -1, -1):
#     if volum_list[N][i] == 1:
#         result = i
#         break

# print(result)


N, S, M = 3, 5, 10
V = [5, 3, 7]

volum_list = [[0]*(M+1) for _ in range(N+1)]
volum_list[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if volum_list[i-1][j] == 0:
            continue
        if j - V[i-1] >= 0:
            volum_list[i][j-V[i-1]] = 1
        if j+V[i-1] <= M:
            volum_list[i][j + V[i-1]] = 1

result = -1

for i in range(M, -1, -1):
    if volum_list[N][i] == 1:
        result = i
        break
    
print(result)