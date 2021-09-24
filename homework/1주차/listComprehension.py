a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

a = list(map(lambda x: str(x+1), list(int(i) for i in a)))

print(a)
