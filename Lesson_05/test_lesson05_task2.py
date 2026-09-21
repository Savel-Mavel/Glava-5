from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
   
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(1)

    input_field = driver.find_element(By.NAME, "custname")
    input_field.send_keys("Савельев Михаил")
    sleep(2)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    sleep(3)

    current_url = driver.current_url
    original_url = "https://httpbin.qa-territory.online/forms/post"
    
    assert current_url != original_url, f"Ошибка: URL не изменился. Текущий URL: {current_url}"
    

except Exception as e:
    print(f"❌ Произошла ошибка: {e}")
finally:
   driver.quit()
    
