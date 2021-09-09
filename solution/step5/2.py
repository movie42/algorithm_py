# 백준 온라인 저지 단계별 문제풀이 5단계 1차원 배열
# https://www.acmicpc.net/step/6
# 2577
# https://www.acmicpc.net/problem/2577

array = [int(input()) for i in range(3)]
num = 1

for i in range(len(array)):
    num *= array[i]

num = list(str(num))

dict = {str(i): 0 for i in range(10)}

for i in range(len(num)):
    dict[num[i]] += 1

for i in range(10):
    print(dict[str(i)])