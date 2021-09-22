# 버블 정렬

import random
data_list = random.sample(range(100), 50)

def bubblesort(data):
    for i in range(len(data)):
        swap = False
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
        if swap == False:
            break
    return data

print(bubblesort(data_list))

