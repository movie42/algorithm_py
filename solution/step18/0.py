# 백준 온라인 저지 단계별 문제풀이 18단계 스텍
# https://www.acmicpc.net/step/11
# 10828
# https://www.acmicpc.net/problem/10828

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
N = int(sys.stdin.readline())

class Stack:
    def __init__(self):
        self.stack = list()
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack) < 1:
            return -1
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        if len(self.stack) > 0:
            return 0
        else:
            return 1
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return -1

stack1 = Stack()

for i in range(N):
    data = sys.stdin.readline().split()
    if data[0] == 'push':
        stack1.push(data[1])
    elif data[0] == 'pop':
        print(stack1.pop())
    elif data[0] == 'size':
        print(stack1.size())
    elif data[0] == 'empty':
        print(stack1.empty())
    elif data[0] == 'top':
        print(stack1.top())


    

        


