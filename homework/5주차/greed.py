# 문제1: 동전 문제
# 지불해야 하는 값이 4720원 일 때 1원 50원 100원, 500원 동전으로 동전의 수가 가장 적게 지불하시오.
# 가장 큰 동전부터 최대한 지불해야 하는 값을 채우는 방식으로 구현 가능
# 탐욕 알고리즘으로 매순간 최적이라고 생각되는 경우를 선택하면 됨

coin_list = [500, 100, 50, 1]


def shop(cash, price):
    a = price
    count = 0
    for i in cash:
        if a == 0:
            break
        b = a // i
        count += b
        a -= b * i
    return count


print(shop(coin_list, 4720))


# 문제2: 부분 배낭 문제 (Fractional Knapsack Problem)
# 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
# 각 물건은 무게(w)와 가치(v)로 표현될 수 있음
# 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음, 그래서 Fractional Knapsack Problem 으로 부름
# Fractional Knapsack Problem 의 반대로 물건을 쪼개서 넣을 수 없는 배낭 문제도 존재함 (0/1 Knapsack Problem 으로 부름)

data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]


def solution(data, k):
    sort_data = sorted(data, key=lambda x: x[1] / x[0], reverse=True)
    weight = k
    max_value = 0
    for i in sort_data:
        if weight - i[0] >= 0:
            max_value += i[1]
            weight -= i[0]
        else:
            b = weight / i[0]
            max_value += b * i[1]
            break
    return max_value


print(solution(data_list, 30))
