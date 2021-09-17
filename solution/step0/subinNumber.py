#
#
# 10539
# https://www.acmicpc.net/problem/10539

n, b = int(input()), list(map(int, input().split()))
a = [b[0]]
for i in range(1, len(b)):
    n = i+1
    a.append(b[i]*n-sum(a))
for i in a:
    print(i, end=" ")
