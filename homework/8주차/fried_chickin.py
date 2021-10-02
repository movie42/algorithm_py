# 작동하지 않음....
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


# print(solution(2, [3, 6], [2, 1], 20))
# print(solution(4, [2, 2, 1, 3], [2, 4, 3, 2], 2))


# 예시 답안
# C=튀겨야하는 치킨 수, clean:각 튀김기 세척 시간 스팩, fry:각 튀김기 작동 시간 스팩, N:튀김기의 대수
def solution2(N, fry, clean, C):
    left = 0
    right = C * max([x+y for x, y in zip(fry, clean)])
    answer = right
    while left <= right:
        mid = (left + right) // 2
        val = 0
        print('left', left, 'right', right, 'mid', mid)
        for f, c in zip(fry, clean):
            val += (mid + c) // (f + c)
        if val >= C:
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1
    return answer


N = 2
fry = [3, 6]
clean = [2, 1]
C = 20
print(solution2(N, fry, clean, C))

N = 4
fry = [2, 2, 1, 3]
clean = [2, 4, 3, 2]
C = 2
print(solution2(N, fry, clean, C))
