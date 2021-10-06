# BOJ
# https://www.acmicpc.net/problem/12865

# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과
# 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와
# 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
# N=4 K=7
# W=6 V13
# 4 8
# 3 6
# 5 12

# N, K = list(map(int, input().split()))
# staff_W_V = []

# for i in range(N):
#     W, V = list(map(int, input().split()))
#     staff_W_V.append((W, V))

# staff_W_V.sort(key=lambda x: x[0], reverse=True)
# max_value = [0]*(K+1)

# for i in range(1, K+1):
#     sum_w = 0
#     for j in staff_W_V:
#         sum_w += j[0]
#         if sum_w > i:
#             break
#         else:
#             max_value[i] += j[1]

# print(max(max_value))


# 틀림
# # N 물건의 개수, K 들수 있는 총 무게
# N, K = map(int, input().split())

# bag = [0]*(K+1)

# for i in range(N):
#     weight, value = map(int, input().split())
#     bag[weight] = value
#     bag[K] = max(bag[K], bag[weight] + bag[weight-1])

# print(bag[K])


# 틀린 이유가... 아마도 가방의 무게의 변화를 계속 초기화하지 않아서 그런것 같다.
# 그러니까. 예를 들어 3을 들었는데 4이면 3과 더할 수 있는거니까 4 = 14가 되어야한다.
# N 물건의 개수, K 들수 있는 총 무게
N, K = map(int, input().split())

bag = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = map(int, input().split())
    for j in range(1, K+1):
        if j < weight:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-weight] + value)

print(bag[N][K])
