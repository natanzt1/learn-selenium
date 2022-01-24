from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://renanstore.co.id/')
driver.find_element_by_xpath("//input[@name='s']").send_keys("iphone 12" + Keys.ENTER)
# driver.find_element_by_xpath("//span[@class='input-group-addon']").click()
time.sleep(2)
test = driver.find_elements_by_xpath("//div[@class='smart_pdtitle']//a")
for x in test:
    print(x.text)


driver.quit()
