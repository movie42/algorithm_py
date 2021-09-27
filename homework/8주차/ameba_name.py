def solution(N):
    answer = 0
    name_list = [0] * (N+1)
    for min in range(N+1):
        if min == 0:
            name_list[min] = 1
        elif min == 1:
            name_list[min] = 2
        elif min == 2:
            name_list[min] = 2
        elif min > 2:
            name_list[min] = name_list[min-1] + name_list[min-2]
        min += 1

    for j in name_list:
        answer += j

    return answer


print(solution(4))
