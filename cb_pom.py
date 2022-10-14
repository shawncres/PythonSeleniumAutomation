from webdrivermanager import *
from Locators_HM import capbanks_locators

def getRIN():
    global RIN
    try:
        RIN = RIN
    except:
        RIN = input('What is the Ants friendly name to attach a Capbank to?: ').strip().upper()

def alreadyhasCB():
    driver.find_element(by=By.XPATH, value=capbanks_locators.search).send_keys(RIN)
    time.sleep(2)
    try:
        driver.find_element(by=By.XPATH, value=capbanks_locators.details_b).click()
        time.sleep(2)
        if RIN in driver.page_source:
            print(f'Capbank already assigned to {RIN}!')
    except:
        time.sleep(2)
        driver.find_element(by=By.XPATH, value=capbanks_locators.search).clear()
    
def setupRI():
    global driver
    driver = startEdgeDriver()
    driver.implicitly_wait(10)
    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    global GUID
    GUID = ''
    driver.get(capbanks_locators.cb_page)

def create():
    driver.find_element(by=By.XPATH, value=capbanks_locators.create).click()
    time.sleep(2)
    global serialnumber
    serialnumber = 'CB' + str(random.randrange(100000000, 199999999, 1))
    driver.find_element(by=By.XPATH, value=capbanks_locators.serial_f).send_keys(serialnumber)
    time.sleep(2)
    driver.find_element(by=By.CSS_SELECTOR, value=capbanks_locators.hwvers_dd).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=capbanks_locators.hwvers_5).click()
    time.sleep(2)
    driver.find_element(by=By.CSS_SELECTOR, value=capbanks_locators.loc_dd).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=capbanks_locators.loc_atta).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=capbanks_locators.save_b).click()

def validate():    
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=capbanks_locators.search).send_keys(serialnumber)
    time.sleep(2)
    if serialnumber in driver.page_source:
        print(f'Capbank created successfully {serialnumber}')
    else:
        print('No match')

def assign():
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=capbanks_locators.details_b).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=capbanks_locators.link).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=capbanks_locators.antselect).send_keys(RIN)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[2]/div/form/div[2]/div/div/div').click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value=capbanks_locators.saveant).click()
    time.sleep(3)
    if RIN in driver.page_source:
        print(f'Capbank assigned successfully to {RIN}')
    else:
        print('No match')
    


    

if __name__=='__main__':
    getRIN()
    setupRI()
    alreadyhasCB()
    create()
    validate()
    assign()
    driver.close()

    
