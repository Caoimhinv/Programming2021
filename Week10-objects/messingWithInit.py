# messing with init
# author: Andrew Beatty lecture

class Person:
    def __init__(self, first, nick, last):
        self.firstname = first
        self.nickname = nick
        self.lastname = last
    def full_name(self):
        if hasattr(self, 'middlename'):
            return self.firstname + ' ' + self.middlename + ' ' + self.nickname + ' ' + self.lastname
        return self.firstname + ' ' + self.nickname + ' ' + self.lastname
    def __str__(self):
        return self.full_name()
    def add_middle_name(self, middlename):
        self.middlename = middlename

if __name__ == '__main__':

    person1 = Person('Caoimhin', 'Valiant', 'Vallely')

    # person1.add_middle_name('Brian')
    print(person1.firstname)
    print(person1.full_name())
    print(person1)