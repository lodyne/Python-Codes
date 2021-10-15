x= [2,3,4,5,6,2,1,2,9]
max=0
var=x[0]
for i in x:
    freq=x.count(i)
    if freq>max:
        max=freq
        var=i
print('most common is:'+str(var))
