def gcdString(a, b):
    str = ""
    if a == b:
        return a
    elif len(a) == 0:
        return ""
    elif len(b) == 0:
        return ""

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            str += a[i]
            i += 1
            j += 1
        else:
            return ""

    if i < len(a) - 1:
        return gcdString(a[i:], str)
    elif j < len(b) - 1:
        return gcdString(b[j:], str)

    return str


A = "ababcde"
B = "ababcde"
print(gcdString(A, B))

A = "ababababab"
B = "abab"
print(gcdString(A, B))

A = "abababab"
B = "abab"
print(gcdString(A, B))

A = "fast"
B = "campus"
print(gcdString(A, B))
