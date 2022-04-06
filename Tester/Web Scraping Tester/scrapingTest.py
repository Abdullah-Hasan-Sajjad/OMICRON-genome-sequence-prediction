import time
from    selenium    import  webdriver
#from   selenium.webdriver.edge.options import  Options
from    selenium.webdriver.common.action_chains import  ActionChains
from    selenium.webdriver.common.by    import  By
from    selenium.webdriver.common.keys  import Keys

driver=webdriver.Edge('D:\SeleniumDrivers\msedgedriver')
driver.get("https://www.epicov.org/epi3/frontend#18d21b")

myUserName="AbdullahRafi"
myPassword="AJYvoWNZ#"

driver.implicitly_wait(3)


# Putting username and password

driver.find_element(By.ID,"elogin").send_keys(myUserName)
ActionChains(driver).perform()

driver.find_element(By.ID,"epassword").send_keys(myPassword)
ActionChains(driver).perform()

ActionChains(driver).send_keys(Keys.ENTER).perform()

# Search click
driver.find_element(By.XPATH,"//div[@class='sys-actionbar-action-ni'][2]").click()

# Putting search values
driver.find_element(By.ID,"ce_r9uykk_hw_entry").send_keys("Asia / Bangladesh / Dhaka")
driver.find_element(By.ID,"ce_r9uykk_i5_select").send_keys("VOC Omicron GRA (B.1.1.529+BA.*) first detected in Botswana/Hong Kong/South Africa")
driver.find_element(By.ID,"ce_r9uykk_hx_entry").send_keys("Human")


time.sleep(4)
position=0+1
xpath="//tbody[@class='yui-dt-data']/tr["+str(position)+"]"
driver.find_element(By.XPATH,xpath).click()

time.sleep(4)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='about:blank']"))
time.sleep(4)
fasta=driver.find_element(By.XPATH, "//pre").text

time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='sys-event-hook sys-form-button']").click()