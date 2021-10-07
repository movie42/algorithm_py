def allConstructor(target, wordBank, memo):
    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []
    for word in wordBank:
        if target.find(word) == 0:
            suffix = allConstructor(target[len(word):], wordBank, memo)
            result += map(lambda x: [word]+x, suffix)

    memo[target] = result
    return result


print(allConstructor('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))
print(allConstructor('abcdef', ['ab', 'abc',
      'cd', 'def', 'abcd', 'ef', 'c'], {}))
print(allConstructor('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
print(allConstructor('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
      ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], {}))
