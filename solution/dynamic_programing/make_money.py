def solution(N, duration, cost):
    dp = [0]*(N+1)

    def dynamic_programming():
        max_val = 0

        for i in range(N-1, -1, -1):
            if duration[i] + i <= N:
                # 다이나믹 프로그래밍은 값을 저장하는게 중요한데
                # 어떻게 저장할지에 대한 아이디어를 떠올리는게 중요하다.
                dp[i] = max(cost[i] + dp[i+duration[i]], dp[i+1])
            else:
                dp[i] = dp[i+1]
        max_val = dp[0]
        return max_val

    result = dynamic_programming()
    return result


N = 7
duration = [3, 5, 1, 1, 2, 4, 2]
cost = [10, 20, 10, 20, 15, 40, 200]
print(solution(N, duration, cost))

N = 10
duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
print(solution(N, duration, cost))
