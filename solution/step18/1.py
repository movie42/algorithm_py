# 백준 온라인 저지 단계별 문제풀이 18단계 스텍
# https://www.acmicpc.net/step/11
# 10773
# https://www.acmicpc.net/problem/10773

N = int(input())

stack = list()

for i in range(N):
    number = int(input())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))
