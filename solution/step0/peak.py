import math

def solution(x):
    i = math.floor(len(x)/2)
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

    

        

print(solution([-1, -1, -1, -1, 0, 1, 20, 19, 17]))
