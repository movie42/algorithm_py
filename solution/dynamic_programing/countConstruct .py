def countConstruct(target, wordBank, memo):
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    totalCount = 0

    for word in wordBank:
        if target.find(word) == 0:
            restNumber = countConstruct(target[len(word) :], wordBank, memo)
            totalCount += restNumber

    memo[target] = totalCount
    return memo[target]


# print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"], {}))
# print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
# print(countConstruct('skateboard', [
#       'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
# print(countConstruct('enterapotentpot', [
#       'a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
# print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
#       ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], {}))


def countConstruct_tab(target, wordBank):
    table = [0] * (len(target) + 1)
    table[0] = 1
    for i in range(len(table)):
        for word in wordBank:
            if target[i : i + len(word)] == word:
                table[i + len(word)] += table[i]
    return table[len(target)]


print(countConstruct_tab("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    countConstruct_tab(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
