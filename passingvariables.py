from webdrivermanager import *
from Locators_HM import ri_locators




class variable_test():
    RIN = 'x'

    def __init__(self):
        pass
    
    def updateRIN(self, x):
        setattr(self, 'RIN', x)











if __name__=='__main__':
        
    test = variable_test()
    print(test.RIN)
    test.updateRIN('AG745')
    print(test.RIN)
