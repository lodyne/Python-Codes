class User:
    firstname='Lody'
    lastname='Mtui'

    def username(self):
        print( f'My name is {self.firstname} {self.lastname}.')


class Main:
    obj=User()
    obj.username()

