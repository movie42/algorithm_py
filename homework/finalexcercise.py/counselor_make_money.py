def solution(N, duration, cost):
    cost_load_map = [0]*(N+1)
    result=[]
    day_cost = [(d, c) for d, c in zip(duration, cost)]
    for i in range(N-1, -1, -1):
        cost_load_map = [0]*(N+1)
        j = i
        while j >= 0:
            d, c = map(int, day_cost[j])
            if j + d > N:
                break
            else:
                j -= d
                cost_load_map[j] += c
        print(cost_load_map)
        result.append(sum(cost_load_map))
    result = max(result)
    return result


N = 7
duration = [3, 5, 1, 1, 2, 4, 2]
cost = [10, 20, 10, 20, 15, 40, 200]
print(solution(N, duration, cost))

N = 10
duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
print(solution(N, duration, cost))