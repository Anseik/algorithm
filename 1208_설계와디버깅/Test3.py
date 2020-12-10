test3 = 'ASADADAS'

def search():
    for i in range(len(test3)):
        print(test3[i], end="")
        if i == len(test3) - 1:
            print()
            reverse_search()

def reverse_search():
    for j in range(len(test3) - 1, -1, -1):
        print(test3[j], end="")


search()
