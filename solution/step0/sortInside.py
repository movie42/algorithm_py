#
#
# 1427번
# https://www.acmicpc.net/problem/1427

# array = list(input())
# array = [int(x) for x in array]

# for i in range(len(array)):
#     max_index = i
#     for j in range(i+1, len(array)):
#         if array[max_index] < array[j]:
#             max_index = j
#     array[i], array[max_index] = array[max_index], array[i]

# for i in array:
#     print(i, end="")

# 다른풀이

number = input()

for i in range(9, -1, -1):
    for j in number:
        if i == int(j):
            print(j, end="")
