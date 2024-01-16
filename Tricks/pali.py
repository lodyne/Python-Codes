word = input('ENTER WORD: ')

word = word.casefold()

reverse_word = reversed(word)

if list(word) == list(reverse_word):
    print("the word is pallidrome")
else:
    print("the word is not pallidrome")