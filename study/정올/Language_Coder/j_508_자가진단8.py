title = ['item', 'count', 'price']
item = ['pen', 'note', 'eraser']
count = ['20', '5', '110']
price = ['100', '95', '97']

def add_empty(target):
    empty = 10 - len(target[i])
    for e in range(empty):
        target[i] = ' ' + target[i]

for i in range(len(title)):
    add_empty(title)
    print(title[i], end='')
print()

for i in range(len(item)):
    add_empty(item)
    add_empty(count)
    add_empty(price)
    print(item[i], count[i], price[i], sep='')






