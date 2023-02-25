# Import section
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

# Ini Script utama yang dijalankan sistem
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Ini Script untuk membuka page shopee
web_url = 'https://shopee.co.id/'
driver.get(web_url)
time.sleep(10)

# Ini Script untuk remove pop up banner element di shopee
xpath_popup_banner_close_button = '//*[@id="main"]/div/div[2]/div/shopee-banner-popup-stateful'
element = driver.find_element(By.XPATH, xpath_popup_banner_close_button)
driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)

# Ini Script untuk klik tombol ig di shopee
xpath_ig_button = '//*[@id="main"]/div/header/div[1]/nav/div[1]/div[3]/a[2]'
driver.find_element(By.XPATH, xpath_ig_button).click()
time.sleep(10)

# Script untuk pengecekan apakah page yg dibuka benar halaman ig shopee
# Script untuk mengecek apakah page yang terbuka mengandung expected URL
shopee_ig_tab = driver.window_handles[1]
driver.switch_to.window(shopee_ig_tab)
current_url = driver.current_url
expected_shopee_ig_url = "www.instagram.com/Shopee_ID/"
assert expected_shopee_ig_url in current_url

# Script untuk mengecek apakah page ig yang terbuka sesuai dengan expected ig profile name
ig_profile_name_xpath = '//body/div/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/h2'
ig_profile_name = driver.find_element(By.XPATH, ig_profile_name_xpath).text
expected_shopee_ig_profile_name  = "shopee_id"
assert ig_profile_name == expected_shopee_ig_profile_name

