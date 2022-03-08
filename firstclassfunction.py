# def power(num1,num2):
#     return num1 ** num2

# list1 = [1,2,3,4,5]
# list2 = [2,3,4,5,6]

# pwr = map(power,list1,list2)

# print(pwr)

def plusOne(num):
    return num + 1

def plusTwo(num):
    return num + 2

def plusThree(num):
    return num + 3

list_function = [plusOne,plusTwo,plusThree]

for i in list_function:
    print(i)

print(plusOne(1))
print(plusTwo(1))
print(plusThree(1))