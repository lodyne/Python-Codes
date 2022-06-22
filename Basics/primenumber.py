lower = 2
upper = 20
for primenum in range(lower, upper + 1):
    if primenum > 1:
        for i in range(2,primenum):
            if(primenum % i)==0:
                break
        else:
            print(primenum)
