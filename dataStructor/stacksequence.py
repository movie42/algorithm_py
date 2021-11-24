# 백준 온라인 저지
# https://www.acmicpc.net/problem/1874

# 첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 
# 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 
# n이하의 정수가 하나씩 순서대로 주어진다. 
# 물론 같은 정수가 두 번 나오는 일은 없다.

n = int(input())

count = 1
a = []
stack = []

# push 순서는 반드시 오름차순이어야한다.
# 4 3 6 8 7 5 2 1

for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        a.append('+')
    if stack[-1] == data:
        stack.pop()
        a.append('-')
    else:
        print('NO')
        exit(0)
        
print('\n'.join(a))