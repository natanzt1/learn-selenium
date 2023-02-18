from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://google.co.id/")

keyword = "reebok"
driver.find_element(By.XPATH, "//input[@name='q']").send_keys(keyword + Keys.ENTER)
titles = driver.find_elements(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']")

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