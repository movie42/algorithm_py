# Stack
# LIFO Last In First Out
# 데이터 넣기 : push, 데이터 빼기 : pop
import random

class Stack:
    def __init__(self):
        self.stack_data = []
    
    def push(self, data):
        self.stack_data.append(data)
        return self.stack_data

    def pop(self):
        return self.stack_data.pop()

stack1 = Stack()


