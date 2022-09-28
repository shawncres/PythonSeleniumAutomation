


class person():
    adultage = 18
    def __init__(self, name, age ):
        self.intro = 'This is a person class'
        self.name = name
        self.age = age

    @staticmethod
    def check(self):
        if cls.age < adultage:
            print(f'{self.name} is too young')
        else:
            print(f'{self.name} is an adult')

            






if __name__ == '__main__':
    first  = person('Shawn', 30)
    print(first.intro)
    person.check()
       
