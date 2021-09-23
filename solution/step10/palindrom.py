# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요

def palindrom(str):
    if len(str) <= 1:
        return True
    if str[0] == str[-1]:
        return palindrom(str[1:-1])
    else:
        return False
    
print(palindrom('MOTOR'))