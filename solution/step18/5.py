# 백준 온라인 저지 단계별 문제풀이 18단계 스텍
# https://www.acmicpc.net/step/11
# 17298
# https://www.acmicpc.net/problem/17298

# 스택의 세계는 오묘하구나.... 
# 처음에는 그냥 for문 두개 돌려서 풀었으나... 시간 초과

N = int(input())
A = list(map(int, input().split()))

stack = list()
NGE = [-1 for _ in range(N)]

stack.append(0)

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)

for i in NGE:
    print(i)