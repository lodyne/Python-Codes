def foo( ):
    x=2
    print(x)
foo( )
#print(x)
"""The output shows an error, 
because we are trying to access a local variable x in a global scope 
whereas the local variable only works inside foo() or local scope."""