class Stack():
    def __init__(self):
        self.s = list()
        self.top = -1

    def push(self, v):
        self.s.append(v)
        self.top += 1

    def pop(self):
        value = None
        if self.top != -1:
            value = self.s[self.top]
            self.s = self.s[:self.top]
            self.top -= 1

        return value

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.s)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.s)
