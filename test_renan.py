# Import section
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from function import *

# Ini Script utama yang dijalankan sistem
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Ini Script untuk memanggil fungsi yang dibuat di atas
login_test_with_wrong_username(driver)
