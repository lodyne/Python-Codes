def login(msg):
    def login_message():
        print(f" {msg}")
    return login_message

variable = login('hey')
print(variable)
variable()

# def login(msg):
#     def login_message(info):
#         print(f" {msg}- {info}")
#     return login_message

# variable = login('hey')
# variable('Gud Morning') 
# variable('Gud Afternoon') 

