# 이진 탐색
# 이진 탐색은 데이터가 정렬되어있는 상태에서 진행해야한다.
import random

data_list = random.sample(range(50), 10)
data_list.sort()

def binary_search(data, search_item):
    if len(data) == 1 and data[0] == search_item:
        return True
    if len(data) == 0:
        return False
    while len(data) > 1:
        mid = len(data)//2
        if data[mid] == search_item:
            return True
        if data[mid] > search_item:
            data = data[:mid]
        else:
            data = data[mid:]
    return False

print(data_list)
print(binary_search(data_list, 33))