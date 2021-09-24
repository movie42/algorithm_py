# 아래 기반 코드를 완성하여, 입력받은 값 중 중앙값을 출력하는 클래스를 완성하시오. 입력받은 값이 짝수개이면, 중앙값 2개의 평균을 출력하시오. (단, clear 메소드는 입력받은 내역을 모두 삭제)

class Median:
    def __init__(self):
        self.numberList = []

    def get_item(self, item):
        self.numberList.append(item)
        self.numberList.sort()

    def clear(self):
        self.numberList = []

    def show_result(self):
        mid = len(self.numberList)//2
        if len(self.numberList) % 2 == 0:
            mid2 = mid - 1
            middle = (self.numberList[mid] + self.numberList[mid2])/2
            print(middle)
        else:
            middle = self.numberList[mid]
            print(middle)


median = Median()

for x in range(10):
    median.get_item(x)

median.show_result()

median.clear()

for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)

median.show_result()
