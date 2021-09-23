# 선택정렬
# 작은 값을 선택해서 교환하는 방법으로 정렬
import random
data_list = random.sample(range(100), 10)


def selectSort(data):
    min_index = 0
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]
    return data
    
# print(selectSort(data_list))

# 버블정렬
# 인접한 값을 비교해 교환한다. 교환이 없을 때까지 계속

data_list2 = random.sample(range(100), 10)

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

# print(bubbleSort(data_list2))


# 삽입정렬
# 선택한 하나의 값의 앞보다크고 뒤보다 작을 경우를 찾아 그 사이에 삽입한다. 
data_list3 = random.sample(range(100), 10)
def insertionSort(data):
    for i in range(len(data)-1):
        for j in range(i+1, 0, -1):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
            else:
                break
    return data
            
# print(data_list3)
# print(insertionSort(data_list3))

# 병합정렬
# 쪼갤수 없을 때까지 쪼갠 후에 병합하며 정렬한다. 
data_list4 = random.sample(range(100), 10)

def merge(left_data, right_data):
    sortList = []
    i, j = 0, 0
    while i < len(left_data) and j < len(right_data):
        if left_data[i] < right_data[j]:
            sortList.append(left_data[i])
            i+=1
        elif left_data[i] >= right_data[j]:
            sortList.append(right_data[j])
            j+=1

    while i < len(left_data):
        sortList.append(left_data[i])
        i+=1
    while j < len(right_data):
        sortList.append(right_data[j])    
        j+=1
    return sortList


def splitList(data):
    if len(data) <= 1:
        return data
    mid = len(data)//2
    left = splitList(data[:mid])
    right = splitList(data[mid:])
    return merge(left, right)

# print(splitList(data_list4))

# 퀵정렬
# 마지막 퀵정렬 정렬의 꽃이라고 한다. 기준값으로 나누어 왼쪽은 기준값보다 작은 값으로 오른쪽을 큰값으로 분류해서 합친다. 

data_list5 = random.sample(range(100000), 10000)

def quickSort(data):
    if len(data)<=1:
        return data
    pivot = data[0]
    left, right = list(), list()
    for i in range(len(data)):
        if data[i] > pivot:
            right.append(data[i])
        elif data[i] < pivot:   
            left.append(data[i])
    return quickSort(left)+[pivot]+quickSort(right)

print(quickSort(data_list5))