def solution(N, K1, K2, W, V):
    answer = 0
    k1_weight = K1
    k2_weight = K2
    item_list = []
    for i in range(len(W)):
        item_list.append([W[i], V[i]])
    item_list = sorted(item_list, key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < len(item_list):
        if item_list[i][0] <= k1_weight:
            answer += item_list[i][1]
            k1_weight -= item_list[i][0]
            del item_list[i]
        else:
            i += 1
    while j < len(item_list):
        if item_list[j][0] <= k2_weight:
            answer += item_list[j][1]
            k2_weight -= item_list[j][0]
            del item_list[j]
        else:
            j += 1
    return answer


print(solution(4, 3, 8, [1, 5, 6, 3], [5, 2, 14, 6]))
