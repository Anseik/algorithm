import sys
sys.stdin = open('계산기3.txt')

def change(infix):
    result = []
    stack = []
    # 연산자 우선순위를 어떻게 나타내죠? 딕셔너리로 표현해볼까
    icp = {"(": 3, "*": 2, "+": 1}
    isp = {"(": 0, "*": 2, "+": 1}
    for i in range(len(infix)):
        if "0" <= infix[i] <= "9": # 피연산자이면 result에 넣는다.
            result.append(infix[i])
        elif infix[i] == ")":
            while True:
                tmp = stack.pop()
                if tmp == "(":
                    break
                else:
                    result.append(tmp)

        elif len(stack) == 0: # 스택이 비어있으면 그냥 넣는다.
                stack.append(infix[i])
        elif isp[stack[-1]] < icp[infix[i]]: # 스택의 top에 있는 연산자의 우선순위보다 cal[i]의 우선순위가 높을때 스택에 push한다.
            # 우선순위가 바뀌는 연산자 "("가 있기때문에 isp와 icp를 구분해서 쓴다.
                stack.append(infix[i])
        else: # 스택의 top에 있는 연산자의 우선순위가 cal[i]보다 높거나 같을때
            while isp[stack[-1]] >= icp[infix[i]]: # 연산자의 우선순위가 cal[i]보다 낮아질때까지 pop해서 result에 추가한다.
                result.append(stack.pop())
            stack.append(infix[i])

    while stack: # 스택이 비어있지 않으면
        result.append(stack.pop())

    return result


def calculate(postfix):
    stack = []
    for i in range(len(postfix)):
        if "0" <= postfix[i] <= "9":
            stack.append(int(postfix[i]))
        else:
            x1 = stack.pop()
            x2 = stack.pop
            if postfix[i] == "*":
                y = x2 * x1
                stack.append(y)
            elif postfix[i] == "+":
                y = x2 + x1
                stack.append(y)

    result = stack.pop()
    return result


T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input() # 중위표기법
    # print(N)
    # print(cal)
    postfix = change(infix)
    answer = calculate(postfix)
    print("#{} {}".format(tc, answer))