stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0: # 스택이 비어있는지 항상 고려해야 한다.
        print("Stack is Empty")
        return
    else:
        return stack.pop()


push(1)
push(2)
push(3)
print(stack)
print(pop())
print(pop())
print(pop())
print(stack)