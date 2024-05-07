# map deals with expressions
from functools import reduce


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result1 = map(lambda x: x**2, mylist)
print(list(result1))

# filter deals with conditions
result2 = filter(lambda x: x % 2 == 0, mylist)
print(list(result2))


result3 = filter(lambda x: x % 2 == 1, mylist)
print(list(result3))

# reduce gives single result
result4 = reduce(lambda x, y: x + y, mylist)
print(result4)
