def count(string):
    #string="DBCABA"
    #print(string.split(''))
    #string=list('')

    for i in string:
        if i in string:
            return i
        else:
            string.append(i)

    print(string)

count('DBCABA')