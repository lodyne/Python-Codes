def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info('Math','Coding',name='John',age=25)

def std_info(*args,**kwargs): #accepting the arbitrary number of positional or keywords values
    print(args)
    print(kwargs)
courses=['Math','Coding'] 
info={'name':'Lody','age':21}
std_info(*courses,**info) #Unpacking values and pass them individually
 