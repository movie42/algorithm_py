# 과제
# 문자열 s1, s2, s3가 주어졌을 때, 문자열 s3가 문자열 s1과 s2를 교차로 배치하여 만들어질 수 있는지 여부를 출력하라.

# 스택문제인것같은데....

# 입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 출력: True

# 입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 출력: False

# s3를 stack으로 집어넣고 하나씩 빼면서 s1과 s2에서 순서대로 빠져나올 수 있는지 비교하면 되는 문제같다.

def solution(s1, s2, s3):
    answer = False
    stack, str1, str2 = [i for i in s3], list(s1), list(s2)
    i, j, k = 0, 0, 0
    order = 1
    while j < len(str1) and k < len(str2):
        if order == 1:
            if stack[i] == str1[j]:
                answer = True
                i += 1
                j += 1
                order = 2
            elif stack[i] == str2[k]:
                answer = True
                i += 1
                k += 1
                order = 2
            else:
                return False
        elif order == 2:
            if stack[i] == str2[k]:
                answer = True
                i += 1
                k += 1
                order = 1
            elif stack[i] == str1[j]:
                answer = True
                i += 1
                j += 1
                order = 1
            else:
                return False

    if len(str1) > j:
        while len(str1) > j:
            if stack[i] == str1[j]:
                answer = True
                i += 1
                j += 1
            else:
                return False
    elif len(str2) > k:
        while len(str2) > k:
            if stack[i] == str2[k]:
                answer = True
                i += 1
                k += 1
            else:
                return False

    return answer


print(solution("aabcc", "dbbca", "aadbbbaccc"))
