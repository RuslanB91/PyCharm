from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
# my_account=driver.find_element_by_id("menu-item-50")
# my_account.click()

# Вход на сайт
# mail = driver.find_element_by_id("username")
# mail.send_keys("Ruslapan@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("2105RuslanB91")
# login = driver.find_element_by_xpath("//input[@value='Login']")
# login.click()
shop=driver.find_element_by_id("menu-item-40")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
# =========У книги HTML5 WebApp Development" нет возможности добавить в корзину,поэтому сделал все тоже самое только с книгой HTML5 Forms========
Add_to_basket = driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=181']")
Add_to_basket.click()
# Item = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"cartcontents"), "1 item"))

# element = driver.find_elements_by_css_selector("span.cartcontents")
# element_get_text = element.text
# assert element_get_text == "1 item"
basket = driver.find_element_by_id("wpmenucartli")
basket.click()
# driver.execute_script("window.scrollBy(0, 300);")
subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"//td[@data-title='Subtotal']>span"), "₹280.00"))
total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"//td[@data-title='total']>span"), "₹280.00"))
# print(element.text)
# print(Sort)
# book = driver.find_element_by_xpath("//img[@title='Android Quick Start Guide']")
# book.click()
# element = driver.find_element_by_css_selector("del>.woocommerce-Price-amount")
# element_get_text = element.text
# assert element_get_text == "₹600.00"
# element = driver.find_element_by_css_selector("ins>.woocommerce-Price-amount")
# element_get_text = element.text
# assert element_get_text == "₹450.00"
# book = driver.find_element_by_xpath("//img[@title='Android Quick Start Guide']")
# book.click()
# open_book = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@title='Android Quick Start Guide']")) )
# open_book.click()
# cross = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )
# cross.click()
# driver.find_element_by_class_name("orderby").click()
# driver.find_element_by_css_selector("[value='price-desc']").click()
# Sort = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"orderby"), "Sort by price: high to low"))
# print(Sort)
# from selenium.webdriver.support.select import Select # импортируем класс Select или библиотеки webdriver
# element = driver.find_element_by_class_name("orderby")
# select = Select(element)
# select.select_by_value("price-desc")
# Sort = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"orderby"), "Sort by price: high to low"))
# print(Sort)
# driver.execute_script("window.scrollBy(0, 300);")
# HTML_book = driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/product-category/html/']")
# HTML_book.click()
# Count = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cat-item-19>span"), "3"))
# print(Count)
# book = driver.find_element_by_xpath("//img[@title='Mastering HTML5 Forms']")
# book.click()
# title = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div>h1"), "HTML5 Forms"))
# print(title)
driver.quit()
