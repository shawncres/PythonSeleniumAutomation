from webdrivermanager import startChromeDriver
from webdrivermanager import startEdgeDriver
from Locators_HM import ri_locators

global driver


driver1 = startChromeDriver()
driver2 = startEdgeDriver()
url = ri_locators.ri_page


driver1.get(url)
driver2.get(url)
