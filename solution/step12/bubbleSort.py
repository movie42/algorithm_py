# 버블 정렬
# 버블 정렬은 아이디어가 단순하다.

# 데이터가 두 개일 때

arr = [2, 1]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

# 데이터가 세개일 때,
arr2 = [27, 5, 2]
i, N = 0, len(arr)

while i < N:
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

print(arr2)
