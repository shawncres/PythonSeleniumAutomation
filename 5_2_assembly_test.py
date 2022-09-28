from assemblies_pom import *


class TestAntCreation(unittest.TestCase):

    def test_1_assembly(self):
                
        setRIN()
        setupRI()
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

if __name__ == '__main__':
    unittest.main(verbosity=2)
