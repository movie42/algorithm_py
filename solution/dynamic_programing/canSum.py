# 뭐가 다른거지? 
# memo={} 디폴트로 설정하고 돌리면 False가 나오지 않는다!!!??

def canSum(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for number in numbers:
        remainder = targetSum - number
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


# print(canSum(7, [2, 3], {}))
# print(canSum(7, [5, 3, 4, 7], {}))
# print(canSum(7, [2, 4], {}))
# print(canSum(8, [2, 3, 5], {}))
# print(canSum(300, [7, 14], {}))


def canSum_tab(targetSum, numbers):
    table = [False]*(targetSum+1)
    table[0] = True
    for i in range(len(table)):
        if table[i] == True:
            for number in numbers:
                if i + number < len(table):
                    table[i + number] = True
    return table[targetSum]


print(canSum_tab(7, [2, 3]))
print(canSum_tab(7, [5, 3, 4, 7]))
print(canSum_tab(7, [2, 4]))
print(canSum_tab(8, [2, 3, 5]))
print(canSum_tab(300, [7, 14]))