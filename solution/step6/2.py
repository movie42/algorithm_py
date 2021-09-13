# 백준 온라인 저지 단계별 문제풀이 6단계 함수
# https://www.acmicpc.net/step/5
# 1065
# https://www.acmicpc.net/problem/1065

n = int(input())


def solve(num):
    count = 0
    for i in range(1, num+1):
        array = list(map(int, list(str(i))))
        number = []
        if len(array) == 1:
            count += 1
        elif len(array) > 1:
            for i in range(len(array)):
                if i > 0:
                    number.append(array[i] - array[i-1])
            if len(number) == 1:
                count += 1
            elif len(number) > 1:
                sum = 0
                for i in range(len(number)):
                    if i > 0:
                        sum += (number[i] ^ number[i-1])
                if sum == 0:
                    count += 1
    return count


print(solve(n))
