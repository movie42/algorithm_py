# 백준 온라인 저지
# https://www.acmicpc.net/problem/2920

#  cdefgabC 8음계 c,1,d,2 C8
# 1~8 차례대로 ascending, 8~1 descending 둘다 아니면 mixed
# 입력 첫줄에 8개의 숫자가 주어진다. 
# 출력 첫줄에 ascending, descending, mixed 출력

num = list(map(int, input().split()))

ascending = True
descending = True

for i in range(len(num)-1):
    if num[i] > num[i+1]:
        ascending = False
    if num[i] < num[i+1]:
        descending = False


if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
    
