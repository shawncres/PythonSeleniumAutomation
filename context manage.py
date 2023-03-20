import re
from contextlib import contextmanager



class Corrector():
    def __init__(self, string):
        self.string = string

    @contextmanager
    def capitalize(self):
        try:            
            yield self.string.title()
        finally:
            pass

phrase = 'werwerwe. werewrwer'

x = Corrector(phrase)

with x.capitalize() as b:
    print(b)

##
##x = Corrector(phrase)
##
##print(x.capitalize())

