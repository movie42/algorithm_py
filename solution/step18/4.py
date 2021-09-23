# 백준 온라인 저지 단계별 문제풀이 18단계 스텍
# https://www.acmicpc.net/step/11
# 1874
# https://www.acmicpc.net/problem/1874

# 간단하게 풀 수 있을 것 같은데... 다른 사람들 풀이를 봐야겠다...


def stackFunc():
    n = int(input())
    stack_list = list()
    other_stack = list()
    result_list = list()

    for i in range(n):
        number = int(input())
        stack_list.append(number)

    i = 1
    while i <= n:
        if other_stack and other_stack[-1] == stack_list[0]:
            other_stack.pop()
            stack_list.pop(0)
            result_list.append('-')
        else:
            other_stack.append(i)
            i += 1
            result_list.append('+')
        
    for i in range(len(stack_list)):
        if stack_list[0] != other_stack[-1]:
            result_list = ['NO']
            return result_list
        else:
            other_stack.pop()
            stack_list.pop(0)
            result_list.append("-")
    
    return result_list

data_list = stackFunc()

for i in data_list:
    print(i)