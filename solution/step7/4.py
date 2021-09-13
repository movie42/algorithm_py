# 백준 온라인 저지 단계별 문제풀이 7단계 문자열
# https://www.acmicpc.net/step/7
# 1157
# https://www.acmicpc.net/problem/1157

str = list(input().upper())
dict = {}
max = float('-inf')
maxStr = ""
for i in str:
    if dict.get(i) == None:
        dict[i] = 1
    else:
        dict[i] += 1

for key, value in dict.items():
    if max < value:
        maxStr = key
        max = value
    elif max == value:
        maxStr += key

if len(maxStr) == 1:
    print(maxStr)
elif len(maxStr) > 1:
    print("?")
