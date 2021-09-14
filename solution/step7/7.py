# 백준 온라인 저지 단계별 문제풀이 7단계 문자열
# https://www.acmicpc.net/step/7
# 2941
# https://www.acmicpc.net/problem/2941

str = input()
string = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in string:
    str = str.replace(i, "0")

print(len(str))