# 리스트 값 전부 더하기
reader = [10, 60, 20, 33, 55, 25, 64, 83, 523, 54, 87, 84, 56, 84]

# 반복문으로 더하기
sum_list = 0

for i in reader:
    sum_list += i
print(sum_list)

# sum() 쓰기
print(sum(reader))
