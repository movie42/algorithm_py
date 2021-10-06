# BOJ
# https://www.acmicpc.net/problem/9251
# ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

# str1 = input()
# str2 = input()

# 문제를 이해를 못했다.... 이게 아니다.
# 순서를 고려해야한다.
# dict1 = {}
# for i in str1:
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#         dict1[i] += 1

# dict2 = {}
# for i in str2:
#     if i not in dict2:
#         dict2[i] = 1
#     else:
#         dict2[i] += 1

# count = 0

# for i in dict2:
#     if i in dict1:
#         print(i, "dict1[i]", dict1[i], "dict2[i]", dict2[i])
#         count += min(dict1[i], dict2[i])
#         print(count)
# print(count)

str1 = input()
str2 = input()

n, m = len(str1), len(str2)

lcs_table = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            lcs_table[i][j] = lcs_table[i-1][j-1] + 1
        else:
            lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1])

print(lcs_table[n][m])
