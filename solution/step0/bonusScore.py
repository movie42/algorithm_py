#
#
# 17389
# https://www.acmicpc.net/problem/17389

N, S = int(input()), input()

score = 0
bonusScore = 0
for i in range(N):
    if S[i] == "O":
        bonusScore += 1
        score += i + bonusScore
    else:
        bonusScore = 0
print(score)
