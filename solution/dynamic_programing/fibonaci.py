# 피보나치

# 함수 재귀로 풀이
def fibonaci(n):
    if n == 1 or n == 2:
        return 1
    return fibonaci(n-1) + fibonaci(n-2)

# 동적 프로그래밍


def fibonaci_dyn(n):
    data_array = [0]*(n+1)
    for number in range(1, n+1):
        if number == 1 or number == 2:
            data_array[number] = 1
        else:
            data_array[number] = data_array[number-1] + data_array[number-2]
    print(data_array)
    return data_array[n]


print(fibonaci(4))
print(fibonaci_dyn(10))
