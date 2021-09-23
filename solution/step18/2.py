# 백준 온라인 저지 단계별 문제풀이 18단계 스텍
# https://www.acmicpc.net/step/11
# 9012
# https://www.acmicpc.net/problem/9012

N = int(input())

ps_stack = []

for i in range(N):
    ps_stack = []
    ps_list = list(input())
    for i in ps_list:
        if i == "(":
            ps_stack.append(i)
        else:
            if len(ps_stack) > 0:
                ps_stack.pop()
            else:
                ps_stack.append(i)
                break
    if len(ps_stack) == 0:
        print("YES")
    else:
        print("NO")