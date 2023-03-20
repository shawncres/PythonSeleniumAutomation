from webdrivermanager import *




from Locators import srr_locators


global driver
driver = startEdgeDriver()
driver.implicitly_wait(10)



driver.get("https://attabotics-hivemind-test.azurewebsites.net/commissioning/software_releases")



##
##name = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/form/div[1]/div[3]/div/div[2]/div[1]').text
##driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/form/div[1]/div[3]/div/div[2]/div[1]').click()
swrnames=[]
entities = range(1,7,1)
for i in entities:
    time.sleep(2)
    driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > div > button').click()
    time.sleep(2)
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.ui.dimmer.modals.page.transition.visible.active > div > div.content > form > div.four.fields > div:nth-child(3) > div > i').click()
    time.sleep(2)     
    selection = f'/html/body/div[2]/div/div[2]/form/div[1]/div[3]/div/div[2]/div[{i}]'
    name = driver.find_element(by=By.XPATH, value=selection).text
    driver.find_element(by=By.XPATH, value=selection).click()
    nameField = driver.find_element(by=By.XPATH, value=srr_locators.srr_Name)
    nameFieldVers = name+'Vers'+'-'+'1.'+str(random.randrange(1,9,1))+'.'+str(random.randrange(1,9,1))+'.'+ str(random.randrange(1,9,1))
    swrnames.append(nameFieldVers)
    nameField.send_keys(nameFieldVers)
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.ui.dimmer.modals.page.transition.visible.active > div > div.content > form > div.four.fields > div:nth-child(4) > div > i').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/form/div[1]/div[4]/div/div[2]/div[3]').click()
    

    time.sleep(2)
##    driver.find_element(by=By.CSS_SELECTOR, value='body > div.ui.dimmer.modals.page.transition.visible.active > div > div.content > form > div:nth-child(3) > div > div.ui.tab.segment.attached.active > div > div > div > div > i').click()
##    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/form/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]').click()



    robotRange = range(1,16,1)

    for i in robotRange:
        try:
            time.sleep(2)
            FieldVers = '1.'+str(random.randrange(0,9,1))+'.'+str(random.randrange(1,9,1))+'.'+ str(random.randrange(1,9,1))
            Field = f'/html/body/div[2]/div/div[2]/form/div[3]/div/div[2]/div/div[{i}]/div/input'
            driver.find_element(by=By.XPATH, value=Field).send_keys(FieldVers)
        except NoSuchElementException:
            try:
                time.sleep(1)
                driver.find_element(by=By.CSS_SELECTOR, value='body > div.ui.dimmer.modals.page.transition.visible.active > div > div.content > form > div:nth-child(3) > div > div.ui.tab.segment.attached.active > div > div:nth-child(1) > div > div > i').click()
                time.sleep(1)
                ##Robot version 4 is 22.2 8 is 4.3
                driver.find_element(by=By.CSS_SELECTOR, value='body > div.ui.dimmer.modals.page.transition.visible.active > div > div.content > form > div:nth-child(3) > div > div.ui.tab.segment.attached.active > div > div > div > div > div.menu.transition > div:nth-child(4)').click() 
                driver.find_element(by=By.CSS_SELECTOR, value='body > div.ui.dimmer.modals.page.transition.visible.active > div > div.content > form > div:nth-child(3) > div > div.ui.tab.segment.attached.active > div > div:nth-child(1) > div > div > i').click()
            except NoSuchElementException:
                break

    time.sleep(2)
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.ui.dimmer.modals.page.transition.visible.active > div > div.actions > button.ui.positive.button').click()
    time.sleep(4)


driver.get("https://attabotics-hivemind-test.azurewebsites.net/commissioning/software_releases")
time.sleep(6)
for i in swrnames:
    if i in driver.page_source:
        print(f'{i} created succussfully!')
    else:
        pass
    
    


    
    
    
    

    
    

