



def handle():
    while True:
        for i in range(2,5,1):
            read = f'/html/body/div[2]/div[103]/div[2]/div/div[i]/div[2]/div/input'
            send = f'/html/body/div[2]/div[103]/div[2]/div/div[i]/div[1]/div/input'
            vers = driver.find_element(by=By.XPATH, value=read).text
            driver.find_element(by=By.XPATH, value=send).send_keys(vers)
