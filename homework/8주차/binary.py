# 예시 답안
# 조건에 맞는 진수를 구하는 문제
def solution(N, start, end, counts):
    mapper = {
        str(x): x for x in range(10)
    }

    offset = len(mapper)
    mapper.update({
        chr(x): x - ord('a') + offset for x in range(ord('a'), ord('z') + 1)
    })

    offset = len(mapper)
    mapper.update({
        chr(x): x - ord('A') + offset for x in range(ord('A'), ord('Z') + 1)
    })

    def todec(s):
        val = 0
        for i, n in enumerate(s[::-1]):
            val += mapper[n] * N**i
        return val

    answer = 0

    start = todec(start)
    end = todec(end)
    for s, target in zip(counts, range(start, end + 1)):
        print(todec(s))
        if todec(s) != target:
            answer += 1

    return answer


N = 13
start = '9'
end = 'd'
counts = ['9', 'a', 'c', 'd', 'e']
print(solution(N, start, end, counts))

N = 62
start = 'Z'
end = '12'
counts = ['Z', '10', '11', '12'] 
print(solution(N, start, end, counts))