# import sys
# sys.stdin = open('123.txt', 'r')

# 10진수 num을 36진수로 변환하는 함수
def to_36(num):
    if num <10:
        return str(num)
    else:
        return chr(num+55)

# 36진수 num을 10진수로 변환하는 함수
# 여기서 int('36진수', 36)을 써서 안 썼으나, 만약 이게 안되면 이 함수 쓰자.
def to_ten(num):
    if num in '0123456789':
        return int(num)
    else:
        return ord(num) - ord('A') + 10 # ord('A') = 65

n = int(input())
numbers = [input() for _ in range(n)] #['GOOD', 'LUCK', 'AND', 'HAVE', 'FUN']
k = int(input())

decimal = [[i, 0] for i in range(36)]# tuple로 했더니 값 변경이 안되서 리스트로 했다.
# print(decimal)

# 각 숫자가 실제 나타내는 10진수 값을 decimal에 넣는다. 인덱스가 수/ 값이 그 수가 실제로 나타내는 값
for num in numbers:
    cnt = 0
    for i in range(len(num)-1, -1, -1):
        tennum = int(num[i], 36)
        decimal[tennum][1] += (36 ** cnt)
        cnt += 1

print(decimal)

# 최댓값을 구하는 거니까, 35로 바꿨을 때 차이가 가장 많이 나는 수(즉, 합이 가장많이 증가하는 수) 부터
# k개 만큼 바꾼다.

# 내림차순 정렬(그냥 내림차순이 아니라 z로 바꿨을 때 값이 제일 큰 순으로 )
ordered_decimal = sorted(decimal, key = lambda x : -((35 * x[1]) - (x[0] * x[1])) )
# print(ordered_decimal)

count = 0
for i in range(36):
    if count == k:
        break
    if ordered_decimal[i][0] != 35:
        ordered_decimal[i][0] = 35
        count += 1

#print(ordered_decimal)

sum = 0
for j in range(36):
    sum += ordered_decimal[j][0] * ordered_decimal[j][1]
#print(sum)

# sum을 36진수로 변환해서 출력
bit = ''
while sum//36: # 여기를 sum >0으로 해버리면 맨 앞에 0이 나옴 ex.0132ZAQA5
    r = to_36(sum % 36)
    bit = r + bit
    sum = sum // 36
bit = to_36(sum) + bit # 마지막에 이거 빼먹지 말기.

print(bit)