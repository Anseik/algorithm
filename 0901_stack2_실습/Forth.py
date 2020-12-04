import sys
sys.stdin = open('Forth.txt')

def forth(code):
    stack = []
    for i in range(len(code)):
        if code[i] != "+" and code[i] != "-" and code[i] != "*" and code[i] != "/" and code[i] != ".":
            stack.append(int(code[i]))

        elif code[i] != ".": # 연산자
            if len(stack) >= 2:
                x1 = stack.pop()
                x2 = stack.pop
                if code[i] == "+":
                    y = x2 + x1
                    stack.append(y)
                elif code[i] == "-":
                    y = x2 - x1
                    stack.append(y)
                elif code[i] == "*":
                    y = x2 * x1
                    stack.append(y)
                elif code[i] == "/":
                    y = x2 // x1 # /를 하면 연산결과가 float로 나오기때문에 //를 사용
                    stack.append(y)

            else:
                return 'error'

        elif code[i] == ".":
            if len(stack) != 1: # 피연산자가 더 많은 경우도 있으므로 연산을 끝냈을때 스택에 남아있는 요소 개수를 확인한다.
                return 'error'
            return stack.pop()

T = int(input())
for tc in range(1, T+1):
    code = input().split()
    # print(code)

    result = forth(code)
    print("#{} {}".format(tc, result))
