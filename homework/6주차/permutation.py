# permutaion으로 순열을 전부 구할 경우 메모리를 과다하게 사용하기 때문에
# 적합하지 않다고 한다.

# 탐욕법을 이용해 조합을 구하는 문제
# 예시답안
# k번째 섞은 값을 구하는 문제
# 경우의 수를 전부 구해보면서 규칙은 찾았지만 구현을 잘 하지 못했던 문제다..
# 주어진 답을 잘 공부해서 구현 능력을 길러봐야겠다.

def solution(n, k):
    # 조합할 수 있는 수의 개수 0은 초기화
    # 숫자가 1개이면 1개 2개이면 2개 3개이면 6개 4개이면 24개 5개면 120개....
    fact = {0: 1}

    # 이건... 조합의 개수다. 숫자가 4개일 경우 한가지 숫자를 root로
    # 구할 수 있는 조합의 개수는 총 6개이다.factorial의 방법으로 늘어난다.
    def factorial(num):
        if num in fact:
            return fact[num]
        val = factorial(num - 1) * num
        fact[num] = val
        return val

    # 1번째 조합 가능한 숫자 [1,2,3,4]
    seq = [i for i in range(1, n + 1)]

    # 우리가 구하려는 수는 9번째 조합이다.
    # 9번째 수를 구한다면 9//6이면 = 1이다.
    # 그러나 문제는... 예를 들어서 6번째 수를 구한다고 하면 1이다.
    # 그래서 규칙에 안맞는다.예외의 경우가 생기니까 그래서 1을 빼면
    # 0 -5, 6-11로 가니까 9번째 수일 경우 root가 2인 숫자 안에서 찾을 수 있게 된다.
    remainder = k - 1

    ans = []
    #
    for i in range(n - 1, 0, -1):
        div = factorial(i)
        # 숫자를 찾는 방법
        val = remainder // div
        # 나머지는 예를 들어 9번째 수라고 하면 val을 구하는 과정에서 root가 2인 경우를 찾았으니까.
        # 2인경우에서 순서대로 0,1,2,3,4,5에서 다음 가지수를 찾으면 된다.
        # 그래서 6가지 경우 수 안에서 remainder를 찾는 것
        remainder %= div
        # 조합의 가지수가 순서대로 되기 때문에 이 경우가 성립한다.
        ans.append(seq[val])
        del seq[val]
    # 마지막에 남은 숫자 하나를 맨 뒤에 넣어준다.
    ans.append(seq[0])
    # 결과
    return ans


# print(solution(3, 3))
print(solution(4, 1))
