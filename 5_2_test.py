from webdrivermanager import *
from Locators_HM import ri_locators
from ri_pom_class import *

#testing script importing pom and set up utilizing pytest sucessfully
## HOLDER variable correctly stores the RIN locally for subsequent tests to use

class TestAntCreation(unittest.TestCase):
    HOLDER = ''
    def test_1_ri(self):
        test1 = roboident()
        print(test1.RINtest)
        test1.setupRI()
        test1.checkWO()
    ##    woQR()
        test1.createRI()
        test1.generateGUID()
        test1.v52gen_assembly()
        test1.WO_entry()
        test1.radiofield_900()
        test1.save_ri()    
        test1.checkRIN()
        print(test1.RINtest)
        setattr(self, 'HOLDER', test1.RINtest)
        print(self.HOLDER)

    def test_2_assembly(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)

