# is_empty(): Queue가 비어있으면 True, 비어있지 않으면 False를 반환한다.
# put(): Queue의 rear에 새로운 데이터를 입력한다.
# get(): Queue의 front에서 데이터를 반환한다. 출력한 데이터는 Queue에서 삭제한다. 더이상 출력할 데이터가 없는 경우 None을 반환한다.
# peek(): Queue의 front에서 데이터를 반환한다. 반환한 데이터는 Queue에 그대로 유지한다. 반환할 데이터가 없는 경우 None을 반환한다.


# 예시 답안 왜 이렇게 단순하게 만들 수 있는데 복잡하게 생각했을까.
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def put(self, data):
        if self.rear is None:
            self.front = Node(data)
            self.rear = self.front
            return self.rear
        else:
            self.rear = Node(data, self.rear, None)
            self.rear.prev.next = self.rear

    def get(self):
        if self.front == None:
            return None
        elif self.front is self.rear:
            data = self.front.data
            self.front, self.rear = None, None
        else:
            data = self.front.data
            self.front = self.front.next
            self.front.prev = None
        return data

    def peek(self):
        if self.front is None:
            return None
        else:
            return self.front.data


# Test code
queue = LinkedQueue()

print(queue.is_empty())

for i in range(10):
    queue.put(i)
print(queue.is_empty())

for _ in range(11):
    print(queue.get(), end=' ')
print()

for i in range(20):
    queue.put(i)
print(queue.is_empty())

for _ in range(5):
    print(queue.peek(), end=' ')
print()

for _ in range(21):
    print(queue.get(), end=' ')
print()
print(queue.is_empty())
