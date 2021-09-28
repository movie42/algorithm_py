# n개의 정수로 이루어진 리스트 nums와 정수 target이 주어졌을 때, nums에 있는 정수 4개를 합하여 target을 만들 수 있는 모든 조합을 구하시오.
# 단, 정답에는 동일한 정수 조합이 여러개 포함되어서는 안된다.

from itertools import combinations
nums = [1, 0, -1, 0, -2, 2]
target = 0


def solution(nums, target):
    result = []
    nums.sort()
    permute = list(combinations(nums, 4))
    sum = 0
    for i in permute:
        sum = 0
        for j in i:
            sum += j
        if(sum == 0):
            result.append(list(i))
            result.sort(key=lambda x: x[0], reverse=True)
    return result


print(solution([1, 0, -1, 0, -2, 2], 0))
