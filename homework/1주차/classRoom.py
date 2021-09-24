
a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer',
     'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']
b = {}

for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1

for key, item in b.items():
    print(key, item)

# 예시 답안
# [count 메서드](https://blockdmask.tistory.com/410)
for sport in set(a):
    print(sport, a.count(sport))
