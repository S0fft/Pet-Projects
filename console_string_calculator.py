example = input("Example: ")

lst = []
first_num = ''
for char in example:
    if char != '+':
        first_num += char
    else:
        lst.append(int(first_num))
        first_num = ''

lst.append(int(first_num))
print(type(sum(lst)))
