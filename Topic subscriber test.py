## Can only be run against Test and not Feature test environment as it is not
## enabled in -test-feature-


from webdrivermanager import *
from Locators_HM import ri_locators
from ri_pom_class import *
import assemblies_pom_class
from assemblies_pom_class import *
import time


##driver.find_element(by = By.XPATH, value='' ).click()


driver = startEdgeDriver()
driver.implicitly_wait(10)
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


def rincap():
    RIN = input('what is the rin?')

##    subassembly page to unparent 
##    https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/149270-FG785-33214#hierarchy

##    unparent button
    driver.find_element(by = '//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div[3]/div/div[3]/button' ).click()
    time.sleep(4)


    
GUID = ''

def asssort():
    driver.get('https://attabotics-hivemind-test.azurewebsites.net/commissioning/assemblies')
    time.sleep(20)

    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[2]/div/div/div/div[3]/div/button[1]').click()
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/thead/tr/th[6]/a/span' ).click()

    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/tbody/tr[1]/td[1]/a/i' ).click()

    time.sleep(4)

    assserial = driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div[1]').text
    print(assserial)
    global extrin
    extrin = assserial.split('-')[1]

    print(extrin)
    getGUID(extrin)

    time.sleep(5)
    parentingSA(assserial)


def getGUID(ex):
    '''Uses preset RIN to extract the GUID to be used in later parenting logic'''
    global GUID
    driver.get(ri_locators.ri_page)
    time.sleep(3)
    driver.find_element(by = By.XPATH, value=ri_locators.searchbox).send_keys(ex)
    driver.find_element(by = By.XPATH, value=ri_locators.searchBtn).click()
    time.sleep(3)
    GUID = driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div[3]/table/tbody/tr/td[1]').text  
    print(GUID)

def parentingSA(i):
    '''Assembles all the subassemblies using the serial lists that was previously generated'''
    driver.get(assemblies_locators.parent_page)
    time.sleep(3)

    time.sleep(5)
    snfield1 = driver.find_element(by=By.XPATH, value=assemblies_locators.sn1_field)
    snfield1.send_keys(GUID)
    time.sleep(3)
    snfield2 = driver.find_element(by=By.XPATH, value=assemblies_locators.sn2_field)
    snfield2.send_keys(i)
    time.sleep(6)
    parentButton = driver.find_element(by=By.XPATH, value=assemblies_locators.parentchild_but)
    parentButton.click()
    time.sleep(6)
    driver.get(assemblies_locators.parent_page)




if __name__ == '__main__':
    asssort()
