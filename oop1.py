class Mimi:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.email=fname+ ''+lname+ '@gmail.com'
        #print(self.email.lower())
        
    
    def full_name(self):
        return '{} {}'.format(self.fname,self.lname)
        #print('{} {}'.format(self.fname,self.lname))
    
    def display(self):
        return 'Name:{} Age:{} Email:{}'.format(self.full_name(),self.age,self.email.lower())
        #print ('Name:{} Age:{} Email:{}'.format(self.full_name(),self.age,self.email.lower()))
        
    
m=Mimi('Lody','Mtui',25)

print(m.full_name())
print(m.display())
#m.full_name()
#m.display()

