from webdrivermanager import *
import time



driver = startEdgeDriver()
driver.implicitly_wait(10)
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)



driver.get('https://attabotics-hivemind-test.azurewebsites.net/commissioning/assemblies')


