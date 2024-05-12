def get_data():
    for i in range(10):
        yield i
    yield -1


def process(data):
    print(data)


# gen = get_data()
# # print(gen)
# # print(next(gen))
# # print(gen.__next__())
# data = next(gen)
# while data != -1:
#     process(data)
#     data = next(gen)

# walrus (assign + process inline)
gen = get_data()
while (data := next(gen)) != -1:
    # while (data := next(get_data())) != -1: # only print values 0 thus call function get_data in every while loop
    process(data)


def f(x):
    return x - 1


results = [f(x) for x in range(10) if f(x) > 3]
walrus_results = [b for x in range(10) if (b := f(x)) > 3]
print(results)
print(walrus_results)