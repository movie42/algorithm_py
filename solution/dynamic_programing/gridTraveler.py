# 그리드 여행자
# 1 : 여행자, 9 : 목적지
# 가는 방법
# 1 0 0 
# 0 0 0
# 0 0 9

# 재귀
def gridTraveler(m, n):
    if m == 1 and n ==1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveler(m-1, n) + gridTraveler(m,n-1)

# 동적 프로그래밍
def gridTraveler_dyn(m, n, memo):
    key = f"{m},{n}"

    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = gridTraveler_dyn(m-1, n, memo) + gridTraveler_dyn(m, n-1, memo)
    return memo[key]

# print(gridTraveler(1,1))
# print(gridTraveler(2,1))
# print(gridTraveler(1,2))
# print(gridTraveler(3,3))
# print(gridTraveler(5,5))
# print(gridTraveler(10,10))
# print(gridTraveler(18,18))

print(gridTraveler_dyn(1,1,{}))
print(gridTraveler_dyn(2,1,{}))
print(gridTraveler_dyn(1,2,{}))
print(gridTraveler_dyn(3,3,{}))
print(gridTraveler_dyn(5,5,{}))
print(gridTraveler_dyn(10,10,{}))
print(gridTraveler_dyn(18,18,{}))