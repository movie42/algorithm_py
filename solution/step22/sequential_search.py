# 순차탐색

import random

data_list = random.sample(range(100), 10)


def sequential_search(data, item):
    for index in range(len(data)):
        if data[index] == item:
            return index
    return -1


print(sequential_search(data_list, 4))
