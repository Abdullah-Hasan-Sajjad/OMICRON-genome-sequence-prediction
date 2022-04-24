from    selenium    import  webdriver
#from   selenium.webdriver.edge.options import  Options
from    selenium.webdriver.common.action_chains import  ActionChains
from    selenium.webdriver.common.by    import  By
from    selenium.webdriver.common.keys  import Keys

driver=webdriver.Edge('D:\SeleniumDrivers\msedgedriver')
driver.get("https://usis.bracu.ac.bd/academia/")

myUserName="rafiabdullahhasansajjad@gmail.com"
myPassword="1@aA66"

# Putting username and password

driver.find_element(By.ID,"username").send_keys(myUserName)
ActionChains(driver).perform()

driver.find_element(By.ID,"password").send_keys(myPassword)
ActionChains(driver).perform()

ActionChains(driver).send_keys(Keys.ENTER).perform()

driver.get("/academia/studentCourse/showAdvising")