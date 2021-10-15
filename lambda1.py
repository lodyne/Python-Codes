# def fun(x):
#     return x+1
# print(fun(2))

g=lambda x: x+1
print(g(2))

name=lambda n: f'My name is {n}' 
print(name('lodyne'))

full_name=lambda fn,ln: print(f"My first name is {fn} and my last is {ln}")
full_name('Lody', 'Mtui')