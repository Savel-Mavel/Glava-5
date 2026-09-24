
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#start button")))
    
    start_btn.click()

    finish_msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#finish h4")))

    driver.save_screenshot("dynamic_loading_result.png")

    assert finish_msg.text == "Hello World!", f"Ожидался 'Hello World!', но получен '{finish_msg.text}'"

    driver.quit()