
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://httpbin.qa-territory.online/")
    sleep(1)

    link = driver.find_element(By.LINK_TEXT, "HTML Form") 
    link.click()
    sleep(3)

    assert driver.current_url.endswith("/forms/post"), f"URL не изменился: {driver.current_url}"
  
    driver.back()
   
    sleep(1)

    expected_url = "https://httpbin.qa-territory.online/"
    assert driver.current_url == expected_url, f"Не вернулись на главную: {driver.current_url}"
  

finally:
    driver.quit()