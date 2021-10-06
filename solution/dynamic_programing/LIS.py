# https://www.acmicpc.net/problem/11053

N = int(input())
data_list = list(map(int, input().split()))

# 왜 이렇게는 해결할 수 없는걸까? (틀림)
# befor_num = 0
# count = 0

# sort_data = sorted(data_list)
# for i in sort_data:
#     if i > befor_num:
#         befor_num = i
#         count += 1

# # 각 숫자의 길이는 1
# 틀림...
# d = [[0]*(N+1) for _ in range(len(data_list)+1)]


# for i in range(1, N+1):
#     for j in range(1, len(data_list)+1):
#         if data_list[i-1] <= data_list[j-1]:
#             d[i][j] = max(d[i-1][j], d[i][j-1])
#         else:
#             d[i][j] = d[i-1][j-1]+1
# print(d[N][len(data_list)])

d = [1]*N

for i in range(1, N):
    for j in range(0, i):
        if data_list[i] > data_list[j]:
            d[i] = max(d[i], d[j]+1)

print(d[N-1])
