def allConstructor(target, wordBank, memo):
    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []
    for word in wordBank:
        if target.find(word) == 0:
            suffix = allConstructor(target[len(word) :], wordBank, memo)
            result += map(lambda x: [word] + x, suffix)

    memo[target] = result
    return result


print(allConstructor("purple", ["purp", "p", "ur", "le", "purpl"], {}))
print(allConstructor("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"], {}))
print(allConstructor("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print(
    allConstructor(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
        {},
    )
)


def allConstructor_tab(target, wordBank):
    table = [[]] * (len(target) + 1)
    table[0] = [[]]
    for i in range(len(table)):
        for word in wordBank:
            if target[i : i + len(word)] == word:
                table[i + len(word)] = table[i + len(word)] + list(
                    map(lambda x: x + [word], table[i])
                )
    return table[len(target)]


print(allConstructor_tab("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstructor_tab("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstructor_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(
#     allConstructor_tab(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
#     )
# )
