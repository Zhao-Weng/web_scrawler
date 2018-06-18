from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os,time
from selenium.common.exceptions import TimeoutException

path = r"C:\uiuc_subject_file\cs\web_crawler\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get('https://apps.uillinois.edu/selfservice/')
driver.implicitly_wait(5)

driver.find_element_by_link_text('University of Illinois at Urbana-Champaign (URBANA)')\
.click()
driver.implicitly_wait(10)

driver.find_element_by_id("ENT_ID").send_keys('qzhu10')
driver.find_element_by_id("PASSWORD").send_keys('Zqn951028.')
driver.find_element_by_name("BTN_LOGIN").click()
driver.implicitly_wait(10)

driver.find_element_by_link_text("Registration & Records").click()
driver.implicitly_wait(10)
driver.find_element_by_link_text("Classic Registration").click()
driver.implicitly_wait(10)
driver.find_element_by_link_text("Look-up or Select Classes").click()
driver.implicitly_wait(10)
driver.find_element_by_link_text("I Agree to the Above Statement").click()
driver.implicitly_wait(10)
driver.find_element_by_id("term_input_id").find_element_by_xpath\
("//option[@value='120171']").click()
driver.find_element_by_xpath("//input[@value='Submit']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("""//*[@id="subj_id"]/option[173]""").click()
driver.find_element_by_xpath("//input[@value='Course Search']").click()
driver.implicitly_wait(10)

driver.find_element_by_xpath("/html/body/div[3]/table[2]/tbody/tr[20]/td[3]/form/input[30]").click()
driver.implicitly_wait(10) #440 = 36

while True:
    try:
        shit=driver.find_element_by_xpath("//input[@value='64349 120171']")
        break
    except NoSuchElementException:
        print('no seats available yet, trying 428....')
        driver.back()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath("/html/body/div[3]/table[2]/tbody/tr[20]/td[3]/form/input[30]").click()

driver.find_element_by_xpath("//input[@value='64349 120171']").click()
driver.find_element_by_xpath("//input[@value='Register']").click()

print('Course selected')