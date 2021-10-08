def bestSum(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestCombination = None
    for number in numbers:
        remainder = targetSum - number
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination != None:
            combination = remainderCombination + [number]
            if shortestCombination == None or len(combination) < len(
                shortestCombination
            ):
                shortestCombination = combination
    memo[targetSum] = shortestCombination
    return shortestCombination


# print(bestSum(7, [5, 3, 4, 7], {}))
# print(bestSum(8, [2, 3, 5], {}))
# print(bestSum(8, [1, 4, 5], {}))
# print(bestSum(100, [1, 2, 5, 25], {}))


def bestSum_tab(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []
    for i in range(len(table)):
        if table[i] != None:
            for number in numbers:
                if i + number < len(table):
                    combination = table[i] + [number]
                    if not table[i + number] or len(table[i + number]) > len(
                        combination
                    ):
                        table[i + number] = combination
    return table[targetSum]


print(bestSum_tab(7, [5, 3, 4, 7]))
print(bestSum_tab(8, [2, 3, 5]))
print(bestSum_tab(8, [1, 4, 5]))
print(bestSum_tab(100, [1, 2, 5, 25]))
