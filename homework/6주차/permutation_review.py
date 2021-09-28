def permutation(n, k):
    fact = {0: 1}

    def factorial(num):
        if num in fact:
            return fact[num]
        val = factorial(num-1) * num
        return val

    sequence = [i for i in range(1, n+1)]
    answer = []

    reminder = k - 1

    for i in range(n-1, 0, -1):
        divider = factorial(i)
        value = reminder // divider
        reminder %= divider
        answer.append(sequence[value])
        del sequence[value]
    answer.append(sequence[0])

    return answer


print(permutation(4, 9))
