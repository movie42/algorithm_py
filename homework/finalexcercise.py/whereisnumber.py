def solution(array, commands):
    answer = []

    for command in commands:
        cut_list = []
        i, j, k = map(int, command)
        if i == j:
            cut_list = array[i:j+1]
        else:
            cut_list = array[i:j]
        cut_list.sort()
        answer.append(cut_list[k-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))