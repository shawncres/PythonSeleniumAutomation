from webdrivermanager import *
from Locators_HM import ri_locators

class roboident():
    RINtest = 'x'
    def __init__(self):
        pass 
        
    def setupRI(self):
        global driver
        driver = startEdgeDriver()
        driver.implicitly_wait(10)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        global GUID
        GUID = ''
        driver.get(ri_locators.ri_page)

    def checkWO(self):
        global randomWOID
        randomWOID = 'WO' + str(random.randrange(100000,999999,1))
        if randomWOID in driver.page_source:
            randomWOID = 'WO' + str(random.randrange(100000,999999,1))
        else:
            randomWOID == randomWOID
        print(randomWOID)

    def woQR(self):
        global randomWOID
        qrcode.run_example(data=randomWOID)

    def createRI(self):
        driver.find_element(by = By.XPATH, value=ri_locators.create).click()
        

    def generateGUID(self):    
        time.sleep(3)
        driver.find_element(by = By.XPATH, value=ri_locators.generate).click()
        global GUID 
        GUID = driver.find_element(by=By.XPATH, value=ri_locators.GUIDfield).get_attribute('value')
        print(GUID) 

    def updateRIN(self, x):
        setattr(self, 'RINtest', x)

    def v52gen_assembly(self):
        driver.find_element(by=By.CSS_SELECTOR, value=ri_locators.GeneralAssembly).click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value=ri_locators.ant5_2).click()
        driver.find_element(by = By.XPATH, value=ri_locators.RINgenerate).click()

    def v51gen_assembly(self):
        driver.find_element(by=By.CSS_SELECTOR, value=ri_locators.GeneralAssembly).click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value=ri_locators.ant5_1).click()
        driver.find_element(by = By.XPATH, value=ri_locators.RINgenerate).click()

    def v43gen_assembly(self):
        driver.find_element(by=By.CSS_SELECTOR, value=ri_locators.GeneralAssembly).click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value=ri_locators.ant4_3).click()

    def v4namegen(self):
        time.sleep(3)
        randomantname = random.choice(['a', 'b', 'v', 'x']).upper() + random.choice(['a', 'b', 'v', 'x']).upper() + str(random.randrange(10, 99, 1)) + str('5V4')
        driver.find_element(by=By.XPATH, value=ri_locators.v4namefield).send_keys(randomantname)
        
    def WO_entry(self):
        driver.find_element(by=By.XPATH, value=ri_locators.WOnumberfld).send_keys(randomWOID)

    def radiofield_900(self):
        randomRadioID = str(random.randrange(1000,9999,1))+ ':'+ str(random.randrange(1000,9999,1)) + random.choice(['a','b','v','x'])+ str(random.randrange(111,999,1)) 
        driver.find_element(by=By.XPATH, value=ri_locators.radioID).send_keys(randomRadioID)

    def save_ri(self):
        time.sleep(3)
        driver.find_element(by = By.XPATH, value=ri_locators.saveRI).click()
        time.sleep(3)
        if GUID in driver.page_source:
            print('Robot Identity successfully created')    
        else:
            print('Creation of Robot Failed')

    def checkRIN(self):
        time.sleep(3)
        driver.find_element(by = By.XPATH, value=ri_locators.searchbox).send_keys(GUID)
        driver.find_element(by = By.XPATH, value=ri_locators.searchBtn).click()
        time.sleep(3)
        driver.find_element(by = By.XPATH, value=ri_locators.viewassemblyBtn).click()
        time.sleep(3)
        RINfield = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]')
        global RIN
        RIN = RINfield.text
        self.updateRIN(RIN)
        print(RIN)
        time.sleep(2)
        screenshot(driver)




    ##should this include a check on the list page or can this be run prior to a Ant creation to confirm the non reuse of existing WO or split into 2 methods 
    def checkWOconflict(self):
        '''needs to be completed'''
        driver.get(ri_locators.ri_page)
        wo = input('Please enter WO to check: ')
        def check(wo):
            if len(wo.upper()) == 8:
                pass
            elif len(wo.upper()) >= 9:
                print('Too many Charectars for WO')
            else:
                wo = 'WO'+wo
            
        if wo.upper() in driver.page_source:
            print('Succussful check Already used WO not usable')
        else:
            print('Previously unused WO is usable')



if __name__ == '__main__':
    test1 = roboident()
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
    driver.close()

