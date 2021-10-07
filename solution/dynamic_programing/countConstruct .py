def countConstruct(target, wordBank, memo):
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    totalCount = 0

    for word in wordBank:
        if target.find(word) == 0:
            restNumber = countConstruct(target[len(word):], wordBank, memo)
            totalCount += restNumber

    memo[target] = totalCount
    return memo[target]


print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
print(countConstruct('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
print(countConstruct('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
      ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], {}))
