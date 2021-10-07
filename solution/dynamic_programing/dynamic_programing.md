# 동적 프로그래밍

## 개념

> [출처 : 나동빈 이것이 코딩 테스트다 파이썬편](http://www.yes24.com/Product/Goods/91433923)
> 컴퓨터 연산 속도에는 한계가 있다.
> 메모리를 더 써서 속도 문제를 해결 할 수 있는 방법이다.
> 동적 프로그래밍은 그 방법중 하나다.

> 참고한 동영상
> [Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges](https://www.youtube.com/watch?v=oBt53YbR9Kk&t=4209)

## 접근 방법

> [출처 : 나동빈 이것이 코딩 테스트다 파이썬편](http://www.yes24.com/Product/Goods/91433923)
> 큰 문제를 작은 문제로 나눌 수 있다.  
> 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.  
> 문제는 해당 과제가 위에 두 가지 방법을 적용 할 수 있다는 것을 알아야한다.

1. 탑다운
2. 보텀업

## 사용

```python
# 다이나믹 프로그래밍으로 풀어본 피보나치
def fibonaci(n):
    data_array = [0]*(n+1)
    for number in range(n):
        if number == 1 or number ==2:
            data_array[number] = 1
        else:
            data_array[number] = data_array[number-1] + data_array[number-2]


```

동적 프로그래밍은 위와 같이 메모이제이션 기법을 사용해서 해결할 수 있다.

## 유형들

> 점화식을 세울 수 있어야한다.(당연한 말이지만...)
> 초기 값(작은 값 혹은 시작 값)을 어떻게 초기화 시킬것인가.
>
> - 다이나믹 프로그램밍은 작은 값(시작 값)이 큰 값에 영향을 주기 때문에 어떻게 초기화 할지 생각해봐야한다.

다이나믹 프로그래밍 기초

0. [피보나치](./fibonaci.py)
1. [gridTraveler](./gridTraveler.py)
2. [canSum](./canSum.py)
3. [howSum](./howSum.py)
4. [bestSum](./bestSum.py)
5. [canConsruct](./canConstruct.py)

5. [01타일](./01tile.py)
6. [개미전사](./ant_warrior.py)
7. [1로 만들기](./to_one.py)
8. [바닥공사](./floor_construction.py)
9. [LCS](./LCS.py)
10. [LIS](./LIS.py)
11. [보통가방](./nomal_bag.py)
12. [은퇴](./make_money.py)
13. [기타리스트](./maxVolume.py)
14. [효율적인 화폐 구성](./config_money.py)
