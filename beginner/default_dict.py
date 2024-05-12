char_count = {}
string = 'abcdeedcbaaaa'

# for char in string:
#     # print(char)
#     if char not in char_count:
#         char_count[char] = 0
#     char_count[char] += 1
#
# print(char_count)


for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)

# from collections import defaultdict
#
#
# def default():
#     return 0
#
#
# char_count_default_dict = defaultdict(default)
#
# for char in string:
#     char_count_default_dict[char] += 1
#
# print(char_count_default_dict)
