
from ri_pom import *
from assemblies_pom import *



class TestAntCreation(unittest.TestCase):

    def test_1_52total(self):

        setupRI()
        checkWO()
        createRI()
        generateGUID()
        v52gen_assembly()
        WO_entry()
        radiofield_900()
        save_ri()    
        checkRIN()            
                
        getGUID()
        setWO()
        partlist52()
        serialization()
        serialscount()
        parentingSA()
        newchecklists()
        newSAattach()
        antcommission()
        finalization()
        assemblies_pom.assertEqual(serialzerovalidation.text[:1], '0', 'All Sub-assemblies not attached!')
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
