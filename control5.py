#To check if the number is odd/even
print("Enter number")
num=int(input())

if (num%2) ==0:
    print("The number {} is even".format(num))

elif (num%2) ==1:
    print("The number {} is odd ".format(num))

else:
    print("try again")
