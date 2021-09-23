# 1부터 num까지의 곱이 출력되게 만드세요

def multiple(data):
    if data <= 1:
        return 1
    return data * multiple(data-1)

print(multiple(10))