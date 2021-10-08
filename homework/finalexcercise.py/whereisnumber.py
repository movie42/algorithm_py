# 쉬운 문제일수록 조건을 잘 읽어야겠다. ㅜㅠ

def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        copy = array[i-1:j]
        copy.sort()
        answer.append(copy[k-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
