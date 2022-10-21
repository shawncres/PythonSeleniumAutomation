from passingvariables import *
from webdrivermanager import *



class TestAntCreation(unittest.TestCase):



        

    def test_1_passvar(self):
        test = variable_test()
        print(test.RIN)
        test.updateRIN('AG745')
        global RIN
        RIN = test.RIN
        print(RIN)
        self.assertTrue(True)
        
    def test_2_lo_carryover(self):
        print(f'The rin {RIN} has carried over')
        self.assertFalse(True)
        
##        self.assertTrue(self.RIN in locals())
        
    
##    def test_3_gl_carryover(self):
##        print(f'The rin {RIN} has carried over')
##        
##        self.assertTrue(self.RIN in globals())


##    def test_1_RI_manufacturing(self):        
##        setupRI()
##        checkWO()
##    ##    woQR()
##        createRI()
##        generateGUID()
##        v52gen_assembly()
##        WO_entry()
##        radiofield_900()
##        save_ri()    
##        checkRIN()


if __name__ == '__main__':
    unittest.main(verbosity=2)

