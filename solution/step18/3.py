# 백준 온라인 저지 단계별 문제풀이 18단계 스텍
# https://www.acmicpc.net/step/11
# 4949
# https://www.acmicpc.net/problem/4949

while True:
    str = input()
    stack_list = list()

    if str == ".":
        break

    for i in str:
        if i == "(" or i == "[":
            stack_list.append(i)
        elif i == ')':
            if stack_list and stack_list[-1] == '(':
                stack_list.pop()
            else:
                stack_list.append(')')
                break
        elif i == ']':
            if stack_list and stack_list[-1] == '[':
                stack_list.pop()
            else:
                stack_list.append(']')
                break
    if stack_list:
        print("no")
    else:
        print("yes")