# def login(msg):
#     def login_message():
#         print(f" {msg}")
#     return login_message

# variable = login('hey')
# print(variable)
# variable()

# def login(msg):
#     def login_message(info):
#         print(f" {msg}- {info}")
#     return login_message

# variable = login('hey')
# variable('Gud Morning') 
# variable('Gud Afternoon')

def login(msg):
    def login_message(sms):
        print(f" {msg} {sms}")
    return login_message

variable = login('hey')
variable("mambo")