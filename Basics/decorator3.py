def calling_you(func):
    def message():
        print("I'm calling you to tell you that i miss you")
        func()
        print("Ooops thats great")
    return message

@calling_you
def reply_you():
    print("No complains, I'am fine")
reply_you()

# def reply_you():
#     print("No complains, I'am fine")
# resp = calling_you(reply_you)
# resp()