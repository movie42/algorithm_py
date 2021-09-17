import random

number = []
for i in range(6):
    n = random.randint(1, 46)
    if n in number:
        continue
    number.append(n)

number.sort()

print(number)


