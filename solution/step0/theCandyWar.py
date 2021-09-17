#
#
# 9037
# https://www.acmicpc.net/problem/9037

def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1


def teacher(N, candy):
    tem_lst = [0 for i in range(N)]
    for i in range(N):
        if candy[i] % 2:
            candy[i] += 1
        candy[i] //= 2
        tem_lst[(i+1) % N] += candy[i]

    for i in range(N):
        candy[i] += tem_lst[i]

    return candy


def solution(N, candy):
    count = 0
    while not check(N, candy):
        count += 1
        candy = teacher(N, candy)
    print(count)


for i in range(int(input())):
    solution(int(input()), list(map(int, input().split())))
