number = int(input("Enter the number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime")
            break
    else:
        print("prime number")
else:
    print("Not a prime")
