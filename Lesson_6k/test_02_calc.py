import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


def test_calculator_delay():
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        
        
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")
        
        
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()
        
        
        
        result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
        
        
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        
        
        result_text = result_element.text
        assert result_text == "15", f"Expected 15, but got {result_text}"
        
    finally:
        
        driver.quit()