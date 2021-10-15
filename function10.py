def function1(args):
    #print(args)
    '''If there is no expression in the statement or 
    the return statement itself is not present inside a
    function, then the function will return the None object'''
    #return #return None 
    '''The return statement is used to exit a function 
    and go back to the place from where it was called'''
    return args 
print(function1('this is me'))

def function2(mylist):
    mylist=[10,20,30]
    print(mylist)
function2('')

def function3(list):
    '''This function returns
    number given by a list'''
    print(list)
    return
function3(list=[1,2,3])
print(function3.__doc__)

def function4(args1,args2):
    total=args1 + args2
    return total
print(function4(10,20))

def function5(par1,par2):
    product=par1*par2
    return product
product=function5(2,3)
print(product)
    