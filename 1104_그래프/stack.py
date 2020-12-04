class Stack:
    def __init__(self, n):
        self.top = -1 #  초기 값은 데이터가 비어있으니 -1
        self.s = [0] * n

    def push(self, d): # top+1에 데이터를 추가
        if self.top == len(self.s) - 1:
            return False
        self.s[self.top+1] = d
        self.top += 1
        return True

    def pop(self):
        if self.top == -1:
            return None
        value = self.s[self.top]
        self.s[self.top] = 0
        self.top -= 1
        return value

my_stack = Stack(5)
my_stack.push(5)
my_stack.push(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
my_stack.push(1)
print(my_stack.pop())
my_stack.push(1)
print(my_stack.pop())
my_stack.push(1)
print(my_stack.pop())
