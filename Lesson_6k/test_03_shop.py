import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service


def test_shop_purchase():
    
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    try:
        
        driver.get("https://www.saucedemo.com/")
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))
        )
        
        
        username_field = driver.find_element(By.CSS_SELECTOR, "#user-name")
        username_field.send_keys("standard_user")
        
        password_field = driver.find_element(By.CSS_SELECTOR, "#password")
        password_field.send_keys("secret_sauce")
        
        
        login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        login_button.click()
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_list"))
        )
        
        
        
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        
        
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        
        
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        
        
        cart_icon = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        cart_icon.click()
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart_list"))
        )
        
        
        checkout_button = driver.find_element(By.CSS_SELECTOR, "#checkout")
        checkout_button.click()
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name"))
        )
        
        first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys("Михаил")
        
        last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys("Савельев")
        
        postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code.send_keys("662606")
        
        
        continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
        continue_button.click()
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        
        
        total_element = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        total_text = total_element.text
        
        
        total_value = float(total_text.replace("Total: $", "").strip())
        
        
        
        
        expected_total = 58.29
        assert total_value == expected_total, \
            f"Expected total ${expected_total}, but got ${total_value}"
        
        print(f"✓ Итоговая сумма корректна: ${total_value}")
        
    finally:
        
        driver.quit()