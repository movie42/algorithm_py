# 백준 온라인 저지 단계별 문제풀이 6단계 함수
# https://www.acmicpc.net/step/5
# 4673
# https://www.acmicpc.net/problem/4673

def solve():
    sum = 0
    dNumberList = []
    selfNumber = []
    for i in range(10000):
        selfNumber.append(i)
        sum = i
        array = list(map(int, list(str(i))))
        for i in array:
            sum += i
        if sum < 10000:
            dNumberList.append(sum)

    for i in dNumberList:
        if i in selfNumber:
            selfNumber.remove(i)

    return selfNumber


sN = solve()

for i in sN:
    print(i)
