# 백준 온라인 저지 단계별 문제풀이 5단계 1차원 배열
# https://www.acmicpc.net/step/6
# 8958
# https://www.acmicpc.net/problem/8958

n = int(input())

bonusScore = 0
score = 0
scoreArray = []

for i in range(n):
    array = list(input())
    score = 0
    bonusScore = 0
    for index in range(len(array)):
        if array[index] == "X":
            bonusScore = 0
            continue
        elif array[index] == "O":
            score += 1
            if index > 0 and array[index-1] == "O":
                bonusScore += 1
                score += bonusScore
    scoreArray.append(score)

for i in scoreArray:
    print(i)