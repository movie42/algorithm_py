# 백준 온라인 저지 단계별 문제풀이 7단계 문자열
# https://www.acmicpc.net/step/7
# 2941
# https://www.acmicpc.net/problem/2941

str = input()
list = []

if "c=" in str:
    list += str.split('c=')
if "c-" in str:
    list += str.split('c-')
if "dz=" in str:
    list += str.split('dz=')
if "d-" in str:
    list += str.split('d-')
if "lj" in str:
    list += str.split('lj')
if "nj" in str:
    list += str.split('nj')
if "s=" in str:
    list += str.split('s=')
if "z=" in str:
    list += str.split('z=')

print(list)
