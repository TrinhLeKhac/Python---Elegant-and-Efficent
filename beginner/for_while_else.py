# Traditional method with flag
items = ['a', 'b', 'c']

# i = 0
# found = False
#
# while i < len(items):
#     if items[i] == 'z':
#         found = True
#         break
#     i += 1
#
# if found:
#     print('Found it')
# else:
#     print('Not found it')


# while/for else
i = 0
while i < len(items):
    if items[i] == 'z':
        print('Found it')
        break
    i += 1
else:
    print('Not found it')
