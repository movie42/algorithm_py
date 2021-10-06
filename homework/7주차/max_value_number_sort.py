# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 나의 답안
# 이렇게 구현한 이유는 ... 주어진 배열을 조합을 이용해 순서를 전부 구현한 후에 string으로 변환해 합쳤을 때,
# 가장 큰 값을 찾는 방법으로 구현했다.
# 하지만 이렇게 할 경우 조합의 가지수가 늘어날수록... 사용하는 메모리가 미친듯이 늘어나서 비효율적이다.
import itertools


array = [3, 30, 34, 5, 9]


def isMax(arr):
    max = 0
    arr = map(str, arr)
    permutationArray = list(map("".join, itertools.permutations(arr)))
    for i in permutationArray:
        if int(i) > max:
            max = int(i)
    return int(max)


print(isMax(array))

# 예시 답안
def cmp_to_key(mycmp):
    "Convert a cmp= function into a key= function"

    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


# 함수안에서 x, y값을 비교한다. b가 a보다 크면 b, a 순으로 정렬된다.
def compare(x, y):
    a = int(str(x) + str(y))
    b = int(str(y) + str(x))
    return b - a


def solution(numbers):
    # numbers를 sort를 할 때, 함수 cmp_to_key의 결과 값을 따라 정렬을 한다.
    # 당연히 cmp_to_key는 가장 큰 값을 찾는 함수일 것이다.
    numbers.sort(key=cmp_to_key(compare))
    answer = "".join(list(map(str, numbers)))

    if answer[0] == "0":
        answer = str(int(answer))

    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
