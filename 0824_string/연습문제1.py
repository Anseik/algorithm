# 1번 방법
str = 'algorithm'
arr = list(str)
# print(len(arr))
swap = len(arr) // 2
for i in range(swap):
    arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
new_str =''.join(arr)
print('1번 방법')
print(new_str)


# 2번 방법
def str_rev(str):
    # str -> list
    arr = list(str)
    # swap
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    # list -> str
    str = ''.join(arr)
    return str

str = 'algorithm'
str1 = str_rev(str)
print('2번 방법')
print(str1)


# 3번 방법
str2 = 'algorithm'
arr1 = list(str2)
arr2 = reversed(arr1)
str2 = ''.join(arr2)
print('3번 방법')
print(str2)


# 4번 방법
s = 'algorithm'
s = s[::-1]
print('4번 방법')
print(s)


# 5번 방법
# 문자열 뒤집기(뒤에서부터 인덱스로 접근)
a = "Reverse this sentence"
reversed_str = list()
for i in range(len(a)-1, -1, -1):
    reversed_str.append(a[i])
reversed_a = "".join(reversed_str)
print('5번 방법')
print(reversed_a)


# 6번 방법
# 복사
b = a[::-1]
print('6번 방법')
print("b: {}".format(b))


# 7번 방법
## reversed 함수 사용
c = list(reversed(a))
print('7번 방법')
print(''.join(c))

