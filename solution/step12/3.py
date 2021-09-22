# 백준 온라인 저지 단계별 문제풀이 12단계 정렬
# https://www.acmicpc.net/step/9
# 2108
# https://www.acmicpc.net/problem/2108
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

import sys

N = int(sys.stdin.readline())
number_list = []

for i in range(N):
    number_list.append(int(sys.stdin.readline()))
# 산술평균
print(round(sum(number_list)/N))

# 중앙값
sort_list = sorted(number_list)
middle_index = len(sort_list)//2
print(sort_list[middle_index])

# 최빈값
dict = {}
for i in sort_list:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

tuple_list = []
for key, item in dict.items():
    tuple_list.append((key, item))

many_number = sorted(tuple_list, key=lambda item:item[1], reverse=True)

if N > 1 and many_number[0][1] == many_number[1][1]:
    print(many_number[1][0])
else:
    print(many_number[0][0])

# 범위
range_num = int(sort_list[-1]) - int(sort_list[0])
print(range_num)