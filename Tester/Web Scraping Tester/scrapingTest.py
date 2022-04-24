import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver=webdriver.Edge('D:\SeleniumDrivers\msedgedriver')
driver.get("https://www.epicov.org/epi3/frontend#18d21b")

driver.implicitly_wait(3)

# Login

myUserName = "AbdullahRafi"
myPassword = "AJYvoWNZ#"

driver.find_element(By.ID, "elogin").send_keys(myUserName)
ActionChains(driver).perform()

driver.find_element(By.ID, "epassword").send_keys(myPassword)
ActionChains(driver).perform()

ActionChains(driver).send_keys(Keys.ENTER).perform()


# Click search

time.sleep(3)
driver.find_element(By.XPATH, "/html/body/form/div[5]/div/div[2]/div/div[1]/div/div/div[3]").click()


# Pressing enter will remove later
time.sleep(3)
ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(3)


# Putting search values

driver.find_element(By.ID, "ce_ral5pp_bu_entry").send_keys("Asia / Bangladesh / Dhaka")
driver.find_element(By.ID, "ce_ral5pp_c3_select").send_keys("VOC Omicron GRA (B.1.1.529+BA.*) first detected in Botswana/Hong Kong/South Africa")
driver.find_element(By.ID, "ce_ral5pp_bv_entry").send_keys("Human")

# Next page click
for i   in range(7):
    time.sleep(3)
    nextpage_XPATH = "//a[@class='yui-pg-next']"
    driver.find_element(By.XPATH, nextpage_XPATH).click()

# Getting Data

list = [[]]
loop_range = 15
i=0
for j in range(1,31):

    # Clicking row
    time.sleep(3)
    #position = i + 1
    position = j
    row_XPATH = "//tbody[@class='yui-dt-data']/tr[" + str(position) + "]"
    driver.find_element(By.XPATH, row_XPATH).click()

    # Diving into iframe
    time.sleep(3)
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='about:blank']"))
    time.sleep(3)

    # Data taking start

    virus_name_XPATH = "/html/body/form/div[5]/div/div[1]/div/div/table/tbody/tr[2]/td[2]"
    virus_name = driver.find_element(By.XPATH, virus_name_XPATH).text
    list[i].append(virus_name)

    location_XPATH = "/html/body/form/div[5]/div/div[1]/div/div/table/tbody/tr[12]/td[2]"
    location = driver.find_element(By.XPATH, location_XPATH).text
    list[i].append(location)

    AA_Substitutions_XPATH = "/html/body/form/div[5]/div/div[1]/div/div/table/tbody/tr[7]/td[2]"
    AA_Substitutions = driver.find_element(By.XPATH, AA_Substitutions_XPATH).text
    list[i].append(AA_Substitutions)

    fasta = driver.find_element(By.XPATH, "//pre").text
    list[i].append(fasta)

    collection_date_XPATH = "/html/body/form/div[5]/div/div[1]/div/div/table/tbody/tr[11]/td[2]"
    collection_date = driver.find_element(By.XPATH, collection_date_XPATH).text
    list[i].append(collection_date)

    Variant_XPATH = "/html/body/form/div[5]/div/div[1]/div/div/table/tbody/tr[8]/td[2]"
    Variant = driver.find_element(By.XPATH, Variant_XPATH).text
    list[i].append(Variant)

    gender_XPATH = "/html/body/form/div[5]/div/div[1]/div/div/table/tbody/tr[15]/td[2]"
    gender = driver.find_element(By.XPATH, gender_XPATH).text
    list[i].append(gender)

    patient_age_XPATH = "/html/body/form/div[5]/div/div[1]/div/div/table/tbody/tr[16]/td[2]"
    patient_age = driver.find_element(By.XPATH, patient_age_XPATH).text
    list[i].append(patient_age)


    # Back button
    time.sleep(3)
    back_button_XPATH = "//button[@class='sys-event-hook sys-form-button']"
    driver.find_element(By.XPATH, back_button_XPATH).click()

    time.sleep(3)
    driver.switch_to.parent_frame()

    list.append([])
    i=i+1


df = pd.DataFrame(list, columns=['virus_name', 'location', 'AA_Substitutions', 'fasta', 'collection_date', 'Variant','gender', 'patient_age'])
df.to_csv('1to30Page8.csv', index=False)