# 백준 온라인 저지 단계별 문제풀이 12단계 정렬
# https://www.acmicpc.net/step/9
# 2750
# https://www.acmicpc.net/problem/2750

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))


min_index = 0
for i in range(N):
    min_index = i
    for j in range(i+1, N):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
