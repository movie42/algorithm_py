# 백준 온라인 저지 단계별 문제풀이 7단계 문자열
# https://www.acmicpc.net/step/7
# 2675
# https://www.acmicpc.net/problem/2675


k = 0

while True:
    k = 0
    result = []
    try:
        n = list(input().split(' '))
        if len(n) > 1:
            str = list(n[1])
            for i in str:
                k = 0
                while k < int(n[0]):
                    result.append(i)
                    k += 1
            print(''.join(result))
    except:
        break
