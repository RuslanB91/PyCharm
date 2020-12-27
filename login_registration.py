from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_account=driver.find_element_by_id("menu-item-50")
my_account.click()
# Регистрация аккаунта
# reg_mail = driver.find_element_by_id("reg_email")
# reg_mail.send_keys("Ruslapan@mail.ru")
# reg_password = driver.find_element_by_id("reg_password")
# reg_password.send_keys("2105RuslanB91")
# time.sleep(3)
# register = driver.find_element_by_xpath("//input[@value='Register']")
# register.click()

# Вход на сайт
mail = driver.find_element_by_id("username")
mail.send_keys("Ruslapan@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("2105RuslanB91")
login = driver.find_element_by_xpath("//input[@value='Login']")
login.click()
Logout = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-MyAccount-navigation-link--customer-logout>a"), "Logout"))
print(Logout)
driver.quit()
