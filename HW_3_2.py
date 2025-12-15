lst = [12, 3, 4, 10]

if len(lst) > 1:
    lst.insert(0, lst.pop())

print(lst)
