import time

def screenshot(driver):
    time.sleep(3)
    filename = (str(time.ctime())+'.png').replace(' ','_').replace(':', '')                                                               
    path = r'C:\Users\ShawnCooper\pyproj\automationtests\Atta\Screenshots\{}'.format(filename)                                                               
    driver.save_screenshot(path)
    time.sleep(3)
    print(f'Screenshot captured as {filename}')
   

if __name__=='__main__':
    screenshot()
