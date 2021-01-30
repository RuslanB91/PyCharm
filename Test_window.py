from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/WebTable.html")
switch_to=driver.find_element_by_xpath("//a[@href='SwitchTo.html']")
switch_to.click()
wind=driver.find_element_by_xpath("//a[@href='Windows.html']")
wind.click()
button_click=driver.find_element_by_xpath("//a/button")
button_click.click()
current_window = driver.current_window_handle
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.close()
driver.switch_to.window(current_window)
seperate=driver.find_element_by_xpath("//a[@href='#Multiple']")
seperate.click()
button_click=driver.find_element_by_xpath("//button[@onclick='multiwindow()']")
button_click.click()
window_after2 = driver.window_handles[2]
driver.switch_to.window(window_after2)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
current_page = driver.current_url
print(current_page)
wait = WebDriverWait(driver, 10)
number_of_tabs = wait.until(EC.number_of_windows_to_be(3))
print(number_of_tabs )
email=driver.find_element_by_id("email")
email.send_keys("Bob@gmail.com")
btn=driver.find_element_by_id("enterimg")
btn.click()
current_page2 = driver.current_url
print(current_page2)
driver.quit()
