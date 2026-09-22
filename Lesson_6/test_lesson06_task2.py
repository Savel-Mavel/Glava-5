from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
   
   
    driver.get("https://gitflic.ru/")
  
    driver.add_cookie({
        "name": "SESSION",
        "value": "MDU4MWJkNjYtYTUxYi00YTY0LWE0MTEtYWQ3ZGMxMTQ2NDk4",
        "domain": "gitflic.ru"
    })
    
    driver.refresh()
    sleep(3)
    
    driver.get("https://gitflic.ru/user/savel_1")
    sleep(5)
    
    url_1 = driver.current_url
     
    driver.delete_all_cookies()
      
    driver.get("https://gitflic.ru/")
    
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZGRhODY0ZWYtZTlmYS00MTNkLTlkYmEtMjc0OGRhZWQ3YzUy",
        "domain": "gitflic.ru"
    })
   
    driver.refresh()
    sleep(3)

   
    driver.get("https://gitflic.ru/user/savel_2")
    sleep(5)
   
    url_2 = driver.current_url
   
    assert url_1 != url_2, f"Скрипты должны различаться, но оба равны: {url_1}"
   
    driver.quit()

test_session_storage_auth()