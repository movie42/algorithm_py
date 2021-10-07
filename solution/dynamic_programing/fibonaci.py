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
    return data_array[n]

# 동적 프로그래밍2
# 출처 : https://www.youtube.com/watch?v=oBt53YbR9Kk&t=4209


def fibonaci_dyn2(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonaci_dyn2(n-1, memo) + fibonaci_dyn2(n-2, memo)
    return memo[n]

# tabulate fib
# 자바스크립트는 index의 범위를 넘어가도 자동으로 처리하는데 반해 파이썬은 그렇지 못한 것 같다.


def fib_tabulate(n):
    table = [0] * (n+1)
    table[1] = 1

    for i in range(1, n+1):
        if i+2 > n:
            table[i+1] += table[i]
            break
        else:
            table[i+1] += table[i]
            table[i+2] += table[i]

    return table[n]


# print(fibonaci(100))
# print(fibonaci_dyn(100))
# print(fibonaci_dyn2(100))
print(fib_tabulate(6))
print(fib_tabulate(9))
print(fib_tabulate(15))
print(fib_tabulate(100))
