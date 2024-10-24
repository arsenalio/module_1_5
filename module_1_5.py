immutable_var = (10,11,12, False, 'lion', 1.5)
print(immutable_var)
print(type(immutable_var))
immutable_var[3] = True
print(immutable_var) # 'tuple' object does not support item assignment
immutable_list = ([15,16,17,18], True, 'eagle')
immutable_list[0][2] = 20
print(immutable_list)
immutable_list[0][3] = 22
print(immutable_list)
