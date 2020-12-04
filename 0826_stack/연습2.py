

def check(arr):
    for i in range(len(arr)):
        if arr[i] == "(": # push
            stack.append(arr[i])
        elif arr[i] == ")": # pop하고 비교해야 한다.
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if stack : return False
    return True


stack = []
arr1 = "()()((()))"
arr2 = "((()(((()()((()())((())))))"
print(check(arr1))
print(check(arr2))