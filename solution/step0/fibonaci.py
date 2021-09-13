#
#
# 2747
# https://www.acmicpc.net/problem/2747

# 재귀함수 피보나치 그런데 이렇게 풀면 메모리 초과... 매우 연산이 많아짐
# n = int(input())


# def fibonaci(num):
#     if num == 0:
#         return 0
#     if num <= 2:
#         return 1
#     return fibonaci(num-1) + fibonaci(num - 2)


# print(fibonaci(n))

# 반복문으로 풀면 해결 가능
n = int(input())

a, b = 0, 1

while n > 0:
    a, b = b, a+b
    n -= 1
    
print(a)