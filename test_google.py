from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://google.co.id/")

keyword = "reebok"
driver.find_element_by_xpath("//input[@name='q']").send_keys(keyword + Keys.ENTER)
titles = driver.find_elements_by_xpath("//h3[@class='LC20lb MBeuO DKV0Md']")

true = 0
for x in titles:
    title = x.text.lower()
    print(title)
    if keyword in title:
        true = true+1

count = len(titles)
accuracy = true/count
print("True = " + str(true) + "\n")
print("Total = " + str(count) + "\n")
print("Accuracy = " + str(accuracy))

driver.quit()