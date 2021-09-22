# 병합정렬은 리스트를 전부 쪼갠 다음에 합치면서 작은 순서대로 데이터를 넣는것

import random

data_list = random.sample(range(100), 10)

def merge(left, right):
    left_index, right_index = 0, 0
    sort_list = list()

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            sort_list.append(right[right_index])
            right_index += 1
        else:
            sort_list.append(left[left_index])
            left_index += 1

    while len(left) > left_index:
        sort_list.append(left[left_index])
        left_index += 1

    while len(right) > right_index:
        sort_list.append(right[right_index])
        right_index += 1

    return sort_list

def mergeSplit(data):
    if len(data) <= 1:
        return data
    mid = len(data)//2
    left = mergeSplit(data[:mid])
    right = mergeSplit(data[mid:])
    return merge(left, right)

print(mergeSplit(data_list))
