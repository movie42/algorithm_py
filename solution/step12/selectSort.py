import random

def selectSort(data):
    min_index = 0
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

data_list = random.sample(range(100), 50)

print(selectSort(data_list))
