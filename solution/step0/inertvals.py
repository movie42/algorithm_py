# 과제
# intervals구하기
# 입력: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 출력: [[1,6],[8,10],[15,18]]
# 설명: 구간 [1,3]와 [2,6]이 겹치므로, [1,6]으로 병합하였다.

intervalsArry = [[1, 4], [4, 5]]


def intervals(arr):
    n = len(arr)
    first, second = arr[0][0], arr[0][1]
    output = []
    for i in range(1, n):
        m = arr[i]
        for j in range(len(m)):
            if first < m[j] and second >= m[j]:
                second = m[j+1]
                break
            elif first < m[j] and second < m[j]:
                output.append([first, second])
                first, second = m[j], m[j+1]
                break
    output.append([first, second])
    return output


print(intervals(intervalsArry))
