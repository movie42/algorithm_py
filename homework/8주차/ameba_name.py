# 아메바 이름 지어주기
# 피보나치 수열을 동적 계획법(?)으로 푸는 것처럼 접근했다.

# 내 풀이
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


# 예시답안
# 답이 멋있다. DFS, BFS, 그래프와 같은 상상력이 부족한가...?ㅜ
def solution2(N):
    stack = []
    stack.append((0, True))  # (level, ready)
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
print(solution2(N))  # 5

N = 4
print(solution2(N))  # 15

N = 8
print(solution2(N))  # 109


def workContinue():
    for i in range(10):
        if i == 3:
            continue

        print(i, 'hi')


workContinue()
