# 인터벌을 구하는 문제
# 입력 예시1

# 입력: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 출력: [[1,6],[8,10],[15,18]]
# 설명: 구간 [1,3]와 [2,6]이 겹치므로, [1,6]으로 병합하였다.
# 입력 예시 2

# 입력: intervals = [[1,4],[4,5]]
# 출력: [[1,5]]
# 설명: 구간 [1,4]와 [4,5]는 겹치는 것으로 간주한다.

# 나의 풀이
def solution(intervals):
    n = len(intervals)
    first, second = intervals[0][0], intervals[0][1]
    answer = []
    for i in range(1, n):
        m = intervals[i]
        for j in range(len(m)):
            if first < m[j] and second >= m[j]:
                second = m[j + 1]
                break
            elif first < m[j] and second < m[j]:
                answer.append([first, second])
                first, second = m[j], m[j + 1]
                break
    answer.append([first, second])
    return answer


print(solution([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution([[1, 4], [4, 5]]))


# 예시 답안
def solution2(intervals):
    # 정렬을 먼저 한다.
    intervals.sort()

    def merge(x):
        if len(x) <= 1:
            return x
        # to_merge= [[1,3]]
        to_merge = [x[0]]
        # intervals = [[2,6], [8,10], [15, 18]]
        del x[0]
        while len(x) > 0:
            # to_merge[0][1] = 1 intervals[0][0] = 2
            if to_merge[0][1] >= x[0][0]:
                # to_merge = [[1,3], [2,6]]
                to_merge.append(x[0])
                del x[0]
            else:
                # x[0][0] = 8
                break
        # [1, max(map(e:e[1] = 3, 6, target = [[1,3], [2,6]]))]
        # merged = [1, 6]
        merged = [to_merge[0][0], max(map(lambda e: e[1], to_merge))]
        # [1, 6] + merge([[8,10], [15,18]])
        # 레게노...ㅜㅜ 이렇게 아름다울수가...
        return [merged] + merge(x)

    return merge(intervals)


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(solution2(intervals))

intervals = [[1, 4], [4, 5]]
print(solution2(intervals))
