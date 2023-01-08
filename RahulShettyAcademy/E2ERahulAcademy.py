
hello there

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\manth\\Documents\\chromedriver.exe")
driver= webdriver.Chrome(service = service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()
# a[href*='shop'] --> When half value used

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

amount = driver.find_element(By.XPATH, "//*[contains(@class, 'table')]/tbody/tr[1]/td[3]/strong").text
total = driver.find_element(By.XPATH, "//*[contains(@class, 'table')]/tbody/tr[2]/td[5]/h3/strong").text
assert amount == total

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.CSS_SELECTOR, "input[id='country']").send_keys("Ind")
wait = WebDriverWait(driver, 5)
countries = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[class*='btn-success']").click()
assert "Success!" in driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
driver.get_screenshot_as_file("screen.png")
