# 백준 온라인 저지 단계별 문제풀이 5단계 1차원 배열
# https://www.acmicpc.net/step/6
# 2562
# https://www.acmicpc.net/problem/2562

max = float("-inf")

index = 0

for i in range(9):
    num = int(input())
    if max < num:
        max = num
        index = i + 1

print(max)
print(index)
