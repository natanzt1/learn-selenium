from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Ini Fungsi
def run_test_for_search_feature(driver):
    web_url = 'https://renanstore.co.id/'
    open_url(web_url)

    # Ini script untuk memberi input "iphone" pada search box lalu menekan Enter
    driver.find_element(By.XPATH, '//*[@id="searchform"]/div/input').send_keys("iphone" + Keys.ENTER)
    time.sleep(5)

    # Ini script untuk mencari seluruh nama product dari hasil pencarian.
    products = driver.find_elements(By.XPATH, "//div[@class='smart_pdtitle']//a")

    # Ini script untuk melakukan pengecekan pada seluruh product dari hasil pencarian tadi
    for product in products:
        # Ini script untuk mendapatkan text nama product dari masing-masing product. Text nama product ditampung dalam variable product_title
        product_title = product.text.lower()

        # Ini script untuk melakukan pengetesan. Pengetesan dalam bahasa pemrograman biasa menggunakan istilah "Assert".
        # Dalam kasus ini, setiap nama produk harus mengandung kata "iphone"
        assert "iphonee" in product_title

    # Setelah pengetesan selesai, code di bawah adalah untuk exit dari chrome yang dibuka oleh selenium
    driver.quit()

def assert_sidebar(driver):
    web_url = 'https://renanstore.co.id/'
    open_url(web_url)

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/ul/li[1]/i').click()
    menu_title_home = driver.find_element(By.XPATH, "//*[@id='menu-header']/li[1]/a").text.lower()
    tag_name = driver.find_element(By.XPATH, "//*[@id='menu-header']/li[1]/a").tag_name
    assert "home" in menu_title_home
    assert "a" == tag_name
    time.sleep(5)

def open_url(driver, url):
    driver.get(url)
    time.sleep(5)

def login_test_with_wrong_username(driver):
    web_url = 'https://renanstore.co.id/'
    open_url(driver, web_url)
    xpath_login_button = '/html/body/div[2]/div/div[1]/ul/li[3]/a[1]'
    xpath_username_field = "//*[@id='user_login']"
    xpath_password_field = "//*[@id='user_pass']"
    xpath_login_submit_button = "//*[@id='wp-submit']"
    xpath_error_message = "//*[@id='topbox']/div[2]/div"

    # Click tombol login pada halaman home
    driver.find_element(By.XPATH, xpath_login_button).click()

    # Cari textfield username dan inputkan username yang salah
    driver.find_element(By.XPATH, xpath_username_field).send_keys("wrong")

    # Cari textfield username dan inputkan password yang salah
    driver.find_element(By.XPATH, xpath_password_field).send_keys("wrong1234")

    #Click tombol "Masuk"
    driver.find_element(By.XPATH, xpath_login_submit_button).click()

    time.sleep(5)

    # Cari text error message yang muncul setelah gagal login
    error_message = driver.find_element(By.XPATH, xpath_error_message).text.lower()
    expected_error_message = "Email/Password Salah, Silahkan coba lagi.".lower()

    assert expected_error_message in error_message
    print("login_test_with_wrong_username success")
    time.sleep(5)
