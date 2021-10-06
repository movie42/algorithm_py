
# 작동 안함.
# 나는 조합을 하려고 했다. 그러니까 각 기계마다 튀기는 횟수의 조합을 구해서 
# 그 조합중에 가장 작은 값을 찾으려고 했다. 그러나.... 조합을 구하는 방법이 구현이 되지 않았다.
# 그리고 모든 가능의 수를 전부 구한다음에 반복을 통해서 찾는 것이기 때문에 성능이 좋지 않다.(매우 좋지 않다.)
# 따지고 보면 순차 탐색을 사용해서 문제를 풀려고 했던 것이다... 으아... 
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

# 이분 탐색을 이용해서 넓은 범위를 탐색하는 문제라고 한다.
# 특정 시간 안에 목표 달성이 가능한지 아닌지 여부를 구현한 후, 이분 탐색을 이용하면 됩니다.
# 분석해보니 답이 너무 멋지다... 어떻게 이분 탐색으로 구할 생각을 할 수 있을까? 

def solution2(N, fry, clean, C):
    left = 0
    right = C * max([x+y for x, y in zip(fry, clean)])
    answer = right

    while left <= right:
        mid = (left + right) // 2
        val = 0
        for f, c in zip(fry, clean):
            # 여기서 c(청소시간)을 한번 더하는 이유는 마지막에는 청소를 할 필요가 없기 때문이다.
            # 첫번째 기계로 14번, 두번째 기계로 10번을 튀기면 각각 70분씩 걸린다.
            val += (mid + c) // (f + c)
        # 그러나 총 튀기는 횟수가 24번이기 때문에 목표하는 튀김 20번보다 크다.
        if val >= C:
            # 0-----140분에서 
            # 0--69분으로 범위를 좁힌다.
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1
    # 반복하면 찾고자하는 시간이 나온다. (두 기계의 합이 20번인 값)
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
