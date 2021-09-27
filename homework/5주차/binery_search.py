# 이진 탐색법은 정렬된 자료를 탐색하는 데에 사용할 수 있다.
# 이진탐색을 이용하여 인덱스가 낮을 수록 더 작은 값으로 정렬된 2차원 리스트에서
# target을 찾으면 True를 반환하고, target을 찾을 수 없으면 False를 반환하는 프로그램을 작성하시오.

# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 출력: True

# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 출력: False

def searchMatrix(matrix, target):
    new_array = []

    if len(matrix) == 0:
        return False
    elif len(matrix) == 1 and target == matrix[0][0]:
        return True
    elif len(matrix) == 1 and target != matrix[0][0]:
        return False

    for i in matrix:
        new_array += i

    while len(new_array) > 1:
        mid_num = len(new_array)//2
        if target > new_array[mid_num]:
            new_array = new_array[mid_num + 1:]
        elif target < new_array[mid_num]:
            new_array = new_array[:mid_num]
        elif target == new_array[mid_num]:
            return True
    return False


print(searchMatrix([[1]], 2))

print(searchMatrix([
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], 3))

print(searchMatrix([
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], 13))
