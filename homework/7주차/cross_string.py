# 문자열 s1, s2, s3가 주어졌을 때, 문자열 s3가 문자열 s1과 s2를
# 교차로 배치하여 만들어질 수 있는지 여부를 출력하라.

# 입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 출력: True

# 입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 출력: False

# 내 답안
# 음... stack으로 접근하려고 했다. 왠지 오름순차로 된것같아서...
# 하지만 stack으로 접근하면 너무 복잡하고 문제는 교차로 문자를 구성한다고 하는데 안된다.
# 그래서 예외의 경우를 처리해주는데 문제를 풀면서 석연치 않았다.
# 그런데 예시 답안에서 이게 그래프 탐색 문제라고 한다... 와우...
def solution(s1, s2, s3):
    answer = False
    stack, str1, str2 = [i for i in s3], list(s1), list(s2)
    i, j, k = 0, 0, 0

    # order는 순서다. 1이면 str1에서 2면 str2에서...
    order = 1
    while j < len(str1) and k < len(str2):
        if order == 1:
            # 그런데... 규칙을 보니까 일단 먼저 str1에서 검색하고
            # 없으면 str2로 가더라...이건 교차가 아니지 않나?
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


print(solution("aabcc", "dbbca", "aadbbcbcac"))
print(solution("aabcc", "dbbca", "aadbbbaccc"))

# 예시답안 2
def solution2(s1, s2, s3):
    found = False

    def dfs(str1, str2, str3):
        nonlocal found
        # print("str1", str1, "str2", str2, "str3", str3)
        n, m = len(str1), len(str2)
        if found is True:
            return

        if str3 == s3:
            found = True
            return

        # str1 큐라고 생각하고, s3는 행적이라고 생각한다
        # 이렇게 하면 str1과, str2를 순서대로 반복하니까
        # str3가 s3와 같아지면 만들 수 있는거다.

        if n > 0 and str1[0] == s3[len(str3)]:
            dfs(str1[1:], str2, str3 + str1[0])

        if m > 0 and str2[0] == s3[len(str3)]:
            dfs(str1, str2[1:], str3 + str2[0])

    dfs(s1, s2, "")
    return found


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(solution2(s1, s2, s3))

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(solution2(s1, s2, s3))


# s3를 그래프로 만들면 이렇게 되는게 아닐까?

# dfs는 stack과 큐를 이용해서 만듬
# 이렇게는 안되네...
# def dfs(s1, s2, s3):
#     graph = {"a": ["d", "c"], "b": ["c"], "d": ["b"], "c": ["a", "b"]}
#     isString = False
#     will_visit, visited = [], []

#     will_visit.append(s1[0])
#     s1 = s1[1:]
#     will_visit.append(s2[0])
#     s2 = s2[1:]

#     while will_visit:
#         value = will_visit.pop()
#         if value not in visited:
#             visited.append(value)
#             will_visit.extend(graph[value])

#     print(visited)
#     return isString


# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"
# print(dfs(s1, s2, s3))
