# 버블 정렬

import random
data_list = random.sample(range(10000), 10000)

def bubbleSort(data):
    for i in range(len(data)):
        swap = False
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                swap = True
        if not swap:
            break 
    return data

print(bubbleSort(data_list))

