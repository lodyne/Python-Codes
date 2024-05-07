# def result(x):
#     return x**2


# print(result(2))

result = (lambda x: x**2)(4) # noqa: E731
print(result)
