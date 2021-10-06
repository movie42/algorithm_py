# 동적 계획법을 사용해서 피보나치 수열을 구하는 방법으로 구현했다. 
def solution(N):
    answer = 0
    name_list = [0] * (N+1)
    for min in range(N+1):
        if min == 0:
            name_list[min] = 1
        elif min == 1:
            name_list[min] = 2
        elif min == 2:
            name_list[min] = 2
        elif min > 2:
            name_list[min] = name_list[min-1] + name_list[min-2]
        min += 1

    for j in name_list:
        answer += j

    return answer


print(solution(4))

# 그런데 Tree의 특수한 형태를 묻는 문제였다고 한다. 
# DFS... 
# 풀이를 찬찬히 뜯어보면 너무 멋있는 풀이다. 아메바가 분열할때와 쉴때를 True와 False로 나눠서 count를 셌다. 
# 그러면 모든 이름을 셀수 있다.

def solution2(N):
    stack = []
    stack.append((0, True)) # (level, ready)
    count = 1

    while stack:
        level, ready = stack.pop()

        if level >= N:
            continue

        if ready:
            stack.append((level + 1, True))
            stack.append((level + 1, False))
            count += 2
        else:
            stack.append((level + 1, True))

    return count

N = 2
print(solution2(N)) # 5

N = 4
print(solution2(N)) # 15

N = 8
print(solution2(N)) # 109



