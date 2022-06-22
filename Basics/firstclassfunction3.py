def is_called():
    def is_returned():
        print('Hello')
    is_returned()

is_called()

def is_called():
    def is_returned():
        print('World')
    is_returned()

# * assigning with parentheses
call = is_called()
call

# * assigning without parentheses
call = is_called
call()

