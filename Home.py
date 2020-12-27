import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
Selenium_Ruby=driver.find_element_by_xpath("//img[@title='Selenium Ruby']")
Selenium_Ruby.click()
driver.execute_script("window.scrollBy(0, 400);")
REVIEWS=driver.find_element_by_class_name("reviews_tab")
REVIEWS.click()
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)
star=driver.find_element_by_class_name("star-5")
star.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Ruslan")
mail = driver.find_element_by_id("email")
mail.send_keys("Ruslapan@mail.ru")
submit=driver.find_element_by_id("submit")
submit.click()
time.sleep(3)
driver.quit()