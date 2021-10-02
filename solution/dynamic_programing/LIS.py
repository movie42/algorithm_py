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

# 풀이
data_array = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if data_list[j] < data_list[i]:
            data_array[i] = max(data_array[i], data_array[j]+1)

print(max(data_array))
