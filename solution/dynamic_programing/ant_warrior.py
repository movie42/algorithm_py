# 식량창고를 약탈해야한다.
# 그런데 들키지 않으려고 최소 한칸 이상 띄어서 약탈해야한다.
# 최대로 빼앗을 수 있는 식량의 갯수 구하기

# N 식량 창고의 개수 (3<=N<=100)
# K 각 창고에 저장된 식량의 개수


def war(N, K):
    table = [0] * (N + 1)
    table[1] = K[0]
    table[2] = K[1]
    for i in range(3, len(table)):
        table[i] = max(table[i - 1], table[i - 2] + K[i - 1])
    return table[N]


print(war(7, [1, 3, 1, 5, 1, 4, 1]))


# 예시 답안


# 피보나치 수열과 비슷하지만 다르다.
# def war2(N, K):
#     d = [0] * (N + 1)
#     d[1] = K[0]
#     d[2] = max(K[0], K[1])
#     for i in range(3, N + 1):
#         d[i] = max(d[i - 1], d[i - 2] + K[i - 1])
#     return d[N]


# print(war(4, [1, 3, 1, 5]))
