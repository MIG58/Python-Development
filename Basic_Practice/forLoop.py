# For Loop

people = ['John', 'Jeo', 'Mark', 'Jimmy', 'Carl',
          'Jonsy', 'Nancy', 'Peter', 'James', 'Newton', 'Jason']

for i in people:
    print(i, "\t")


def sqr_value(num):
    for n in num:
        sq = n * n
        print("Square of ", n, "is:", sq)


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sqr_value(num)
