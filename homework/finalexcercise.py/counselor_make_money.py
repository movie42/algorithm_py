# 으아... 테이블 갱신이 안된다.
# def solution(N, duration, cost):
#     table = [0] * (N+1)
#     for i in range(N):
#         if i + duration[i] <= N:
#             table[i+duration[i]] = max(table[i] +
#                                        cost[i], table[i+duration[i]])
#         else:
#             table[i] = max(table)

#     return table[N]

def solution(N, duration, cost):
    table = [0] * (N+1)

    for i in range(N-1, -1, -1):
        if i + duration[i] <= N:
            table[i] = max(table[i+duration[i]] +
                           cost[i], table[i+1])
        else:
            table[i] = table[i+1]

    return table[0]


N = 7
duration = [3, 5, 1, 1, 2, 4, 2]
cost = [10, 20, 10, 20, 15, 40, 200]
print(solution(N, duration, cost))

N = 10
duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
print(solution(N, duration, cost))
