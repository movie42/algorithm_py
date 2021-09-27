def solution(N, fry, clean, C):
    answer = float('inf')

    min_time_list = []
    min_time = 0
    times_list = []

    for time in range(C+1):
        times_list.append([time, C-time])

    for time in times_list:
        min_time_list = []
        for i in range(N):
            if time[i] == 0:
                min_time_list.append(0)
            else:
                min_time_list.append(fry[i]*time[i] + clean[i]*(time[i]-1))
        min_time = max(min_time_list)
        if min_time < answer:
            answer = min_time

    return answer


print(solution(2, [3, 6], [2, 1], 20))
print(solution(4, [2, 2, 1, 3], [2, 4, 3, 2], 2))
