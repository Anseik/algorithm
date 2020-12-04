# C style

stack = [0] * 100
top = -1

def push(item):
    global top
    if top > 100 - 1:
        return
    else:
        top += 1
        stack[top] = item

def pop(): # isEmpty인지 주의하자!
    global top
    if top == -1:
        print("Stack is Empty")
        return
    else:
        result = stack[top]
        stack[top] = 0
        top -= 1
        return result

push(1)
push(2)
push(3)
print(stack)
print(pop())
print(pop())
print(pop())
print(stack)