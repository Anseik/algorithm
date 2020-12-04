stack = []

stack.append(1) # push
stack.append(2)
stack.append(3)

print(stack)

if stack: # len(stack) != 0 # 비어있지 않은지 항상 확인하자!!
    print(stack.pop())
if stack: # len(stack) != 0
    print(stack.pop())
if stack: # len(stack) != 0
    print(stack.pop())

print(stack)


