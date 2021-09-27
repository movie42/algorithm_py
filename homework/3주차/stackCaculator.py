# 10 5 + 2 * 3 /
# = 15 2 * 3 /
# = 30 3 /
# = 10


class Stack:
    def __init__(self):
        self.list = list()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()


class Calculator:
    def __init__(self):
        self.stack = Stack()

    def calculate(self, string):
        self.string = string.split()
        for i in self.string:
            if i is "+":
                self.stack.list.append(self.stack.list.pop() + self.stack.list.pop())
            elif i is "-":
                self.stack.list.append(-self.stack.list.pop() + self.stack.list.pop())
            elif i is "/":
                self.stack.list.append(
                    1 / self.stack.list.pop() * self.stack.list.pop()
                )
            elif i is "*":
                self.stack.list.append(self.stack.list.pop() * self.stack.list.pop())
            else:
                self.stack.push(int(i))
        return self.stack.list.pop()


# Test code
calc = Calculator()
print(calc.calculate("4 6 * 2 / 2 +"))
print(calc.calculate("2 5 + 3 * 6 - 5 *"))
