import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    
    driver = webdriver.Edge()
    driver.maximize_window()
    
    try:
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='first-name']"))
        )
        
        
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
        
        for field_name, value in fields.items():
            element = driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']")
            element.clear()
            element.send_keys(value)
        
        
        
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert"))
        )
        
        
        zip_code_element = driver.find_element(By.CSS_SELECTOR, "#zip-code")
        zip_code_class = zip_code_element.get_attribute("class")
        
        
        assert "danger" in zip_code_class or "alert-danger" in zip_code_class, \
            f"Zip code field is not red. Class: {zip_code_class}"
        
        
        green_fields = [
            "#first-name",
            "#last-name",
            "#address",
            "#e-mail",
            "#phone",
            "#city",
            "#country",
            "#job-position",
            "#company"
        ]
        
        for field_selector in green_fields:
            element = driver.find_element(By.CSS_SELECTOR, field_selector)
            element_class = element.get_attribute("class")
            
            
            assert "success" in element_class or "alert-success" in element_class, \
                f"Field {field_selector} is not green. Class: {element_class}"
    
    finally:
        
        driver.quit()