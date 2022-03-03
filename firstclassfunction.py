def power(num1,num2):
    return num1 ** num2

list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]

pwr = map(power,list1,list2)

print(pwr)