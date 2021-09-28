# 마을 판사
# 리스트 trust가 주어졌을 때, trust[i] = [a, b]는
# 고유 번호가 a인 사람이 고유 번호가 b인 사람을 믿는다는 것을 의미한다고 한다.

def trust_judgement(trust, N):
    for i in range(1, N + 1):
        # 만약에 i에 (1,2,3) 해당하는 사람중에 어느 한명이 믿는 사람이 없으면 실행하지 않는다.
        # 예를 들어 3이 아무도 판사라고 믿지 않는다면 코드가 실행되지 않고 다음으로 넘어간다.
        if len(list(filter(lambda x: x[0] == i, trust))) > 0:
            continue
        # N-1은 마을 사람이 총 3명일 때, 서로 다른 2명(A,B)이  한명(C)을 판사라고 믿어야 판사가 있는게 되기 때문에 조건을 그렇게 한 것 이다.
        # 여기로 넘어오면 i를 믿는 사람의 수가 전체 인원-1명이 i를 판사라고 믿는지 확인한다.
        if len(list(filter(lambda x: x[1] == i, trust))) == N - 1:
            return i
    return -1


N, trust = 2, [[1, 2]]
print(trust_judgement(trust, N))
N, trust = 3, [[1, 3], [2, 3]]
print(trust_judgement(trust, N))
N, trust = 3, [[1, 3], [2, 3], [3, 1]]
print(trust_judgement(trust, N))
N, trust = 3, [[1, 2], [2, 3]]
print(trust_judgement(trust, N))
N, trust = 4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
print(trust_judgement(trust, N))
