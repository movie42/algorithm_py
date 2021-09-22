# 백준 온라인 저지 단계별 문제풀이 12단계 정렬
# https://www.acmicpc.net/step/9
# 1427
# https://www.acmicpc.net/problem/1427

num_list = list(map(int, list(input())))
sort_list = sorted(num_list, reverse=True)

for i in sort_list:
    print(i, end="")