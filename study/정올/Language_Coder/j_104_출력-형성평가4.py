my_dict = {
    'kor': 90,
    'mat': 80,
    'eng': 100,
}

s = 0
for key, val in my_dict.items():
    print(key, val)
    s += val
print('sum', '{}'.format(s))
print('avg', '{}'.format(s // len(my_dict)))