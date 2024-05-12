import sys


def gen(n):
    for i in range(n):
        yield i


for item in gen(5):
    print(item)


def csv_reader(file_name):
    for row in open(file_name, 'r'):
        yield row
