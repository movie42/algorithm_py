# 정수로 이루어진 수열 x가 주어졌을 때, x[i-1] < x[i], x[i+1] < x[i]인 x[i]를 피크라고 부른다.
# 수열 x에 피크가 단 하나 반드시 존재할 때, 이 피크를 찾아 출력하는 O(logN) 알고리즘을 구현하시오.
# (단, 수열 x의 길이가 N일 때, 반드시 x[0] <= x[1]이며, x[N-1] <= x[N-2]이다.)

def solution(x):
    i = len(x)//2
    if len(x) > 2:
        left = i - 1
        right = i + 1
        if x[i] > x[left] and x[i] > x[right]:
            return x[i]
        else:
            if x[right] < x[left]:
                return solution(x[:left + 1])
            elif x[left] < x[right]:
                return solution(x[right:])
    else:
        if x[i] > x[i-1]:
            return x[i]
        elif x[i] < x[i-1]:
            return x[i-1]


print(solution([-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]))
print(solution([-1, -1, -1, -1, 0, 1, 20, 19, 17]))
