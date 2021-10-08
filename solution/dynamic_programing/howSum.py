# 재귀
def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for number in numbers:
        remainder = targetSum - number
        result = howSum(remainder, numbers)
        if result is not None:
            return result + [number]
    return None


# print(howSum(7, [2, 3]))
# print(howSum(7, [5, 3, 4, 7]))
# print(howSum(7, [2, 4]))
# print(howSum(8, [2, 3, 5]))
# print(howSum(300, [7, 14]))

# 다이나믹 프로그래밍


def howSum_dyn(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for number in numbers:
        remainder = targetSum - number
        result = howSum_dyn(remainder, numbers, memo)
        if result is not None:
            memo[targetSum] = result + [number]
            return memo[targetSum]

    memo[targetSum] = None
    return None


# print(howSum_dyn(7, [2, 3], {}))
# print(howSum_dyn(7, [5, 3, 4, 7], {}))
# print(howSum_dyn(7, [2, 4], {}))
# print(howSum_dyn(8, [2, 3, 5], {}))
# print(howSum_dyn(300, [7, 14], {}))

# tabulation


def howSum_tab(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []
    for i in range(len(table)):
        if table[i] != None:
            for number in numbers:
                if i + number < len(table):
                    table[i + number] = table[i] + [number]
    return table[targetSum]


print(howSum_tab(7, [2, 3]))
print(howSum_tab(7, [5, 3, 4, 7]))
print(howSum_tab(7, [2, 4]))
print(howSum_tab(8, [2, 3, 5]))
print(howSum_tab(300, [7, 14]))
