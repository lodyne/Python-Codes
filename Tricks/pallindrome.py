print("Enter a pallidrome word")
word = input()
my_string = word.casefold()
rev_string = reversed(my_string)

if list(my_string) == list(rev_string):
    print('This is pallindrome')
else:
    print('This is not pallindrome')