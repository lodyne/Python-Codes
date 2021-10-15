a="hello World"
print(a.capitalize())         #make the first letter capital
print(a.strip())
print(len(a))                 #get the length of the string
print(a.lower())              #make all characters lowercase
print(a.upper())              #make all characters uppercase
print(a.replace("e", "a"))
print(a.split(","))           #make into a list
b='o'
print(a.count(b)) 
print(a.startswith('hello')) #returns True/False depending on starting word
print(a.endswith('d'))       #returns True/False depending on ending word
print(a.find('r'))
print(a.isalpha())           #returns True if all is alphabetic
print(a.isnumeric())         #returns True if all is numeric
print(a.isalnum())           #returns True if all is alphanumeric