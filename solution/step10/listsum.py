# 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요

import random 
data_list = random.sample(range(100), 10)

def listSum(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + listSum(data[1:])

print(listSum(data_list))