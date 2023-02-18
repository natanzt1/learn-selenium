from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from script.ignore.confidential import uname, pw

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://twitter.com/')
keyword= "gojek"


def sleep_func():
    return time.sleep(4)


def login_test(uname):
    sleep_func()
    driver.find_element_by_xpath("//a[@href='/login']").click()
    sleep_func()
    driver.find_element_by_xpath("//input[@autocomplete='username']").send_keys(uname + Keys.ENTER)
    sleep_func()
    driver.find_element_by_xpath("//input[@name='password']").send_keys(pw + Keys.ENTER)
    sleep_func()
    driver.find_element_by_xpath("//div[@aria-label='Account menu']").click()
    sleep_func()
    uname_check = driver.find_element_by_xpath("//li[@data-testid='UserCell']//div[@class='css-1dbjc4n r-18u37iz r-1wbh5a2']//span").text

    if uname.lower() == uname_check.lower():
        driver.find_element_by_xpath(
            "//div[@class='css-1dbjc4n r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af r-lrvibr']").click()
        return True
    else:
        driver.find_element_by_xpath(
            "//div[@class='css-1dbjc4n r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af r-lrvibr']").click()
        return False


def search_test(kwd):
    sleep_func()
    driver.find_element_by_xpath("//a[@data-testid='AppTabBar_Explore_Link']").click()
    sleep_func()
    driver.find_element_by_xpath("//input[@data-testid='SearchBox_Search_Input']").send_keys(kwd + Keys.ENTER)
    sleep_func()
    tweets = driver.find_elements_by_xpath(
        "//div[@class='css-1dbjc4n']//article[@data-testid='tweet']")
    true = 0

    for tweet in tweets:
        # print("tweet:"+tweet.text.lower())
        if kwd in tweet.text.lower():
            true = true + 1
        else:
            true = true

    acc = true/len(tweets)
    # print(acc)
    return acc, tweets


res_login = login_test(uname)
acc_search, tweets = (search_test(keyword))
driver.quit()

