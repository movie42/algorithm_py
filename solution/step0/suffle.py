
# ㅊㅓㅅ버ㄴalsdkjfal;sdkfja;sldkfj
#첫번째 아이디어

# 리스트를 섞고, k번째 섞은 값을 반환하는 문제
# 먼저 n까지의 수를 갖는 리스트 만들기 n = 4이면 list는 [1,2,3,4]
# n이 2라면 1개, 3이면 2가지, 4라면 6가지 5라면 24가지 경우의 수를 한 숫자에서 가질 수 있다.
# 한 숫자당 (n-1)!의 경우의 수를 가진다. 그럼 만약에 n = 5일때, k가 27이면 첫번째 숫자는 2다. 
# k가 (n-1)!보다 작을 경우 (n-2)!에서 몇번째에 해당하는지 찾는다. 그러니까... n=4, k =3이면
# num은 6이고 k는 3이니까. 가됨. 


def factorial(n):
    multiful = 1
    for i in range(n):
        multiful *= i
    return multiful

def solution(n, k):
    array = []
    for i in range(1, n+1):
        array.append(i)
    num = factorial(n-1)

    return []


# 두번째 아이디어
# 이렇게 할 필요가 없었다. 그냥 모든 경우의 수를 다 만들어주는 순열을 만든다음에 k번째를 출력해주면 된다. 
# 여기서 중요한건 순열을 만들 때, 라이브러리를 사용해 만들 수 있느냐 없느냐이다. 
# 없을 경우에는 직접 구현을 해주어야한다. 


