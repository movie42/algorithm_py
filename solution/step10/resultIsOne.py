# 1, 정수 n에 대해
# 2. n이 홀수이면 3 X n + 1 을 하고,
# 3. n이 짝수이면 n 을 2로 나눕니다.
# 4. 이렇게 계속 진행해서 n 이 결국 1이 될 때까지 2와 3의 과정을 반복합니다.

def resultIsOne(number):
    print(number)
    if number == 1:
        return number
    if number%2 == 1:
        return resultIsOne(3*number+1)
    else:
        return resultIsOne(number//2)

print(resultIsOne(3))