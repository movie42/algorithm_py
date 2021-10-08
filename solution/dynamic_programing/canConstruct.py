def canConstruct(target, wordBank, memo):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word) :]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return True
    memo[target] = False
    return False


# print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
# print(canConstruct('skateboard', [
#       'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
# print(canConstruct('enterapotentpot', [
#       'a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
# print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
#       ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], {}))


def canConstruct_tab(target, wordBank):
    table = [False] * (len(target) + 1)
    table[0] = True
    for i in range(len(table)):
        if table[i] == True:
            for word in wordBank:
                if target[i : i + len(word)] == word:
                    table[i + len(word)] = True
    return table[len(target)]


print(canConstruct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    canConstruct_tab(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
