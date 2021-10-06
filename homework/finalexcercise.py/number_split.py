import itertools

def solution(expression):
    operator = []
    stack =[]
    if "+" in expression:
        operator.append("+")
    if "-" in expression:
        operator.append('-')
    if '*' in expression:
        operator.append('*')

    permutation_list= list(itertools.permutations(operator))
    
    for i in permutation_list:
        for j in i:
            expression = list(expression.split(j))
            
    return 0

print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))

