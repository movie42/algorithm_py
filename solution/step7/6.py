# 백준 온라인 저지 단계별 문제풀이 7단계 문자열
# https://www.acmicpc.net/step/7
# 5622
# https://www.acmicpc.net/problem/5622

str = input()
dict = {"ABC": 3, "DEF": 4, "GHI": 5, "JKL": 6,
        "MNO": 7, "PQRS": 8, "TUV": 9, "WXYZ": 10}
time = 0
for i in str:
    for key, value in dict.items():
        if i in key:
            time += value
print(time)
