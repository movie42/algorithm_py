#
#
# 2750번
# https://www.acmicpc.net/problem/2750

n = int(input())
array = list()
for i in range(n):
    array.append(int(input()))

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

for i in array:
    print(i)
