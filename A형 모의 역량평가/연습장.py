arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
test = arr[:]
test[0][1] = 100
print(test)
print(arr)