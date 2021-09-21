# 자료구조와 알고리즘

> start date : 2021년 9월 9일

## 목차

- [자료구조와 알고리즘](#자료구조와-알고리즘)
  - [목차](#목차)
  - [깃 생성 이유](#깃-생성-이유)
  - [세팅 및 사용 방법](#세팅-및-사용-방법)
    - [기본 세팅](#기본-세팅)
    - [사용방법](#사용방법)
  - [단계별 문제 풀이](#단계별-문제-풀이)
    - [Step1 입출력과 사칙 연산](#step1-입출력과-사칙-연산)
    - [Step2 if문](#step2-if문)
    - [Step3 for문](#step3-for문)
    - [Step4 while문](#step4-while문)
      - [try, except](#try-except)
    - [Step5 1차원 배열](#step5-1차원-배열)
      - [리스트 컴프리핸션과 딕셔너리 컴프리핸션](#리스트-컴프리핸션과-딕셔너리-컴프리핸션)
      - [배열 안에서 같은 숫자 찾기(투 포인터)](#배열-안에서-같은-숫자-찾기투-포인터)
        - [풀이](#풀이)
    - [Step11 블루트 포스](#step11-블루트-포스)
      - [모든 경우의 수 다 대입해보기](#모든-경우의-수-다-대입해보기)
    - [Step0 구분 없는 문제](#step0-구분-없는-문제)
      - [문자열을 어떻게 다룰 것인가?](#문자열을-어떻게-다룰-것인가)
  - [부록1. VSC 화면 분할 단축키](#부록1-vsc-화면-분할-단축키)

## 깃 생성 이유

1. 자료구조, 알고리즘 문제를 풀면서 헷갈리는 유형은 계속 헷갈렸다. 그래서 문제를 풀면서 생각했던 아이디어를 단계별로 기록하기 위함이다. 간단하게 말해 오답노트.
2. Python을 공부하면서 공부한 문법을 기록하기 위함이다.

## 세팅 및 사용 방법

### 기본 세팅

1. vsc 설치
2. python3설치
3. 해당 git clone 또는 개인 깃에 레포지토리 생성
4. input.txt, output.txt설정
5. python example.py 생성 후 디버깅 하기
   - fn + F5 또는 command + shift + D, 재생버튼 클릭
6. .vscode안에 생성된 launch.json 세팅
7. example.py, input.txt 작성하기

   ```python
   print(input())
   ```

   input.txt

   ```
   <!-- 직접 입력 -->
   Hello World
   ```

   output.txt

   ```
   <!-- 직접 입력하지 않습니다. -->
   Hello World
   ```

### 사용방법

1. 문제풀이는 해당 링크 또는 문제 풀이에서 주어지는 입력값을 input.txt에 붙여넣기 합니다.
2. 파이썬 파일을 생성한 다음에 문제를 풉니다.
3. 디버깅합니다.
4. output.txt에 출력된 값을 확인합니다.
5. 문제 채점은 해당 문제 출제 기관에서 확인합니다.

## 단계별 문제 풀이

> https://www.acmicpc.net/step

### Step1 입출력과 사칙 연산

기본적인 입출력을 할 줄 아는지 묻는 문제

1. 기본 출력 방법

```python
print()
```

2. 기본 입력 방법

```python

import sys

# 입력값 받기 기본
input()

# sys.stdin.readline()으로 입력값 받기 여러가지 값을 받을 때 속도가 더 빠르다고 한다.
n = sys.stdin.readline()
```

3. 입력 값을 리스트로 받는 방법

```python
# 문자열을 list로 쪼개서 받으려고 할 때,
array = list(input())

# 문자열을 정수 값으로 쪼개서 list로 받으려고 할 때,
array = list(map(int, input().split(' ')))
```

### Step2 if문

```python
# 제어문 if 기본
if True:
    print("True")
else:
    print("False")

# 확장
if n >= 0:
    print("A")
elif n == 1:
    print("B")
else:
    print("else")
```

### Step3 for문

```python
# 0~9까지 출력
for i in range(10):
    print(i)

list = ["python", "javascript", "go"]
# python, javascript, go가 차례로 출력
for i in list:
    print(i)

# list의 길이
length = len(list)

# 0부터 2까지 출력
for i in length:
    print(i)
```

### Step4 while문

#### try, except

> 해당 문제  
> [1.py](./solution/step4/1.py)

입력 값만 주어지고 몇번 테스를 해야하는지 알 수 없을 때, try, except 문법을 모르면 풀 수가 없었다. 만약 input값이 더이상 없으면 except에서 break를 받는다.

> 해답 참조
> [출처 IT is Smart](https://itissmart.tistory.com/53)

```python
# input값은
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6
# 로만 주어져있고 테스트 횟수가 input값으로 주어지지 않음
import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().strip().split(' '))
        print(a + b)
    except:
        break
```

### Step5 1차원 배열

#### 리스트 컴프리핸션과 딕셔너리 컴프리핸션

> 해당 문제  
> [2번](./solution/step5/2.py)  
> **[[Python] list comprehension에 대한 즐거운 이해](https://shoark7.github.io/programming/python/about-list-comprehension-python)**  
> [개발을 해보자, \[python\]파이썬 - 31. 리스트컨프리헨션(ListComprehension)](https://m.blog.naver.com/michael_cho77/221979848665)  
> [제대로 파이썬, 컴프리헨션, 2) 딕셔너리 컴프리헨션](https://wikidocs.net/22797)

배열을 압축해서 표현할 수 있는 방법이다. 파이썬에서 너무 중요한 방법이다.

```python
# 보통 배열을 생성하는 방법 (자바스크립트적인 생각)
array1 = []
for i in range(10):
    array1.append(i)

# 리스트 컴프리핸션
listComprehension = [x for x in range(10)]

# 값을 변환하여 넣기
# 해당 배열에 값을 2씩 곱하여 넣는다.
listComprehensionMutation = [x*2 for x in range(10)]

# 딕셔너리 컴프리핸션
# i값을 문자열로 변환한 다음에 key값으로 사용하고 value는 0을 기본값으로 지정하여 넣는다.
# {"1":0, "2":0 .... "9":0}
dictComprehension = {str(i): 0 for i in range(10)}


```

#### 배열 안에서 같은 숫자 찾기(투 포인터)

> [3번](./solution/step5/3.py)  
> [5번](./solution/step5/5.py)

문제를 단순화 하면 배열 안에서 같은 숫자 찾기 문제라고 생각할 수 있다. 매번 이런 유형의 문제를 풀 때마다 헷갈린다. 그래서 손 코딩을 해보았다. 훨씬 생각이 잘 풀어졌다.

##### 풀이

1. 반드시 리스트는 정렬되어있어야한다. 그래서 같은 숫자를 찾기 전에 정렬을 한다.
2. 포인터 변수 i와 j를 선언한다. 다른 숫자가 얼마나 있는지 count를 선언한다. 자기 자신을 포함해야함으로 count의 초기값은 1이다.
3. 배열 안에서 숫자가 같을 때.
   배열 안에서 i가 가리키는 값과 j가 가리키는 값이 같을 때, i값은 변하지 않고 j값이 변한다.
4. 배열 안에서 숫자가 다를 때
   배열 안에서 i가 가리키는 값과 j가 가리키는 값이 다르면,
   count += 1
   i = j
   j += 1
5. while을 빠져 나오면 count를 출력하면 된다.

손 코딩을 하면서 천천히 생각해보는게 많은 도움이 된다.

### Step11 블루트 포스

#### 모든 경우의 수 다 대입해보기

블루트 포스 같은 문제는 모든 경우의 수를 전부 대입해보아야 풀 수 있는 문제가 대부분이다. 그래서 반복문이 3중이 될 수도 있다. 

하지만 가장 중요한건 구현 능력이다. 구현이 되지 않으면 풀 수 없다.

[해결 못한 문제 - 해결하면 어려웠던 문제로 바꾸기](./solution/step11/3.py)


### Step0 구분 없는 문제

#### 문자열을 어떻게 다룰 것인가?

- 분해해서 조작하기 
  - dict, list, tuple을 이용하여 문자열 조작
- stack이나 queue를 사용해서 이용하기

## 부록1. VSC 화면 분할 단축키

수평 분할 : comand + \
수직 분할 : comand + k, comand + \

[비주얼 스튜디오 코드 화면 분할을 해보자 출처 : 개자이너의 다락](https://ssimplay.tistory.com/421)
