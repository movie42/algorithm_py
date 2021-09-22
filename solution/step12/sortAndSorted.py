# 내장함수 sort와 sorted
# Tim sort https://d2.naver.com/helloworld/0315536
# https://docs.python.org/ko/3/howto/sorting.html

# list.sort()
# list.sort()는 list를 정렬하여 list를 반환한다.
# sort는 리스트에게만 정의됨
a = [5, 2, 3, 1, 4]
a.sort()
print(a)

# sorted()
# sorted(list)는 list를 정렬하여 새로운 list를 반환한다.
data_list = sorted([5, 2, 3, 1, 4])
print(data_list)

# 모든 이터러블(반복가능)에 적용 가능
dict_list = sorted({1:"a", 2:"b", 3:"c", 4:"d"})
print('dict_list', dict_list)

# list.sort()와 sorted()는 모두 비교하기 전에 각 리스트 요소에 대해 호출할 함수(또는 다른 콜러블)를 지정하는 key 매개 변수를 가지고 있습니다.
user_tuples = [('kim', 35), ('ko', 33), ('park', 36), ('lee', 32)]

user_sort = sorted(user_tuples, key=lambda item: item[1])
print("user_sort", user_sort)

# 어트리뷰트를 갖는 객체에서도 작동
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return repr((self.name, self.age))

user_obj = [User('ko', 33), User('kim', 35), User('part', 22), User('lee', 23)]
user_obj_sort = sorted(user_obj, key=lambda user: user.age)
print("user_obj_sort", user_obj_sort)

# operator 모듈 함수
from operator import itemgetter, attrgetter
user_sort2 = sorted(user_tuples, key=itemgetter(1))
print('user_sort2', user_sort2)
user_obj_sort2 = sorted(user_obj, key=attrgetter('age'))
print("user_obj_sort2", user_obj_sort2)


# 오름차순 내림차순
# list.sort()와 sorted()는 모두 불리언 값을 갖는 reverse 매개 변수를 받아들입니다. 내림차순 정렬을 지정하는 데 사용됩니다. 예를 들어, 학생 데이터를 역 age 순서로 얻으려면, 이렇게 합니다
revers_sort = sorted(user_tuples, key=lambda user: user[1], reverse=True)
revers_obj_sort = sorted(user_obj, key=attrgetter('name'), reverse=True)
print('revers_sort', revers_sort)
print('revers_obj_sort', revers_obj_sort)


