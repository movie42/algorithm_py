# 정렬 알고리즘의 꽃
# 단계별 구현

# 리스트 쪼개기
import random 

data_list = [1,2,3,4,5]

pivot = len(data_list)//2

data_left = data_list[:pivot]
data_right = data_list[pivot:]

# print(data_left, data_right)

# 다음 리스트를 맨 앞에 데이터를 pivot 변수에 넣고, pivot 변수 값을 기준으로 작은 데이터는 left 변수에, 그렇지 않은 데이터는 right 변수에 넣기
data_list2 = [4,1,2,5,7]
pivot2 = data_list2[0]
data_left2 =[]
data_right2 =[]

for i in range(1, len(data_list2)):
    if pivot2 > data_list2[i]:
        data_left2.append(data_list2[i])
    else:
        data_right2.append(data_list2[i])

# print(data_left2, data_right2)


data_list3 = random.sample(range(100), 50)
left, right = list(), list()
pivot3 = data_list3[0]

for i in range(1, len(data_list3)):
    if data_list3[i]>pivot3:
        right.append(data_list3[i])
    else:
        left.append(data_list3[i])

# data_list 가 다음 세 데이터를 가지고 있을 때 리스트를 맨 앞에 데이터를 기준으로 작은 데이터는 left 변수에, 그렇지 않은 데이터는 right 변수에 넣고 left, right, pivot 변수 값을 사용해서 정렬된 데이터 출력해보기
data_list4 = [4,3,2]
left, right = list(), list()
pivot4 = data_list4[0]

for i in range(1, len(data_list4)):
    if pivot4 > data_list4[i]:
        left.append(data_list4[i])
    else:
        right.append(data_list4[i])

pivot5 = left[0]
second_left, second_right = list(), list()
for i in range(1, len(left)):
    if pivot5 > left[i]:
        second_left.append(left[i])
    else:
        second_right.append(left[i])

left = second_left + [pivot5] + second_right
data_list4 = left+[pivot4]+right
# print(data_list4)


# quick sort 구현
data_list6 = random.sample(range(100), 10)

def quickSort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left, right = list(), list()

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    return quickSort(left) + [pivot] + quickSort(right)

# print(quickSort(data_list6))

# 다시 구현(이렇게도 할 수 있지 않을까?)
# 그런데 생각해보면 중간 값이 리스트 값중에 가장 작거나 큰 값이 될 수도 있기 때문에 최악의 경우가 될 수도 있다. 어차피 확률상으로는 pivot은 랜덤이니까....
data_list7 = random.sample(range(100), 10)

def quickSort2(data):
    if len(data) <= 1:
        return data
    # pivot을 가운데 값으로 하면 안되나용?(임의의 값)
    pivot=len(data)//2  
    # 리스트 컴프리핸션 사용
    left = [i for i in data if data[pivot] > i]
    right = [i for i in data if data[pivot] < i]
    print(pivot, left, right)
    return quickSort2(left) + [data[pivot]] + quickSort2(right)
        
print(quickSort2(data_list7))