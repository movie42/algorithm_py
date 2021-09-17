#
#
# 15312
# https://www.acmicpc.net/problem/15312
# 힌트 알파벳 획수 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1
# 십의 자리가 0이어도 두 자리로 출력한다

jname, hname = input(), input()
hint = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
nameList = [chr(x) for x in range(65, 91)]
nameDict = dict(zip(nameList, hint))
array = []
for i in range(len(jname)):
    array.append(nameDict[jname[i]])
    array.append(nameDict[hname[i]])

while len(array) > 2:
    array = [array[i]+array[i-1] for i in range(1, len(array))]

array = [str(i)[-1] for i in array]

print(int("".join(array)))
