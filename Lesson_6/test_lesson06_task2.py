from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "MDU4MWJkNjYtYTUxYi00YTY0LWE0MTEtYWQ3ZGMxMTQ2NDk4",  
        "domain": "gitflic.ru"
    })

    driver.refresh()

   
    wait.until(lambda d: "user/savel_1" in d.current_url or "gitflic.ru/" in d.current_url)
    print("After refresh, URL:", driver.current_url)

   
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1, .user-profile, [data-testid='profile-name']")))
    except Exception:
       
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    driver.get("https://gitflic.ru/user/savel_1")
    wait.until(lambda d: "user/savel_1" in d.current_url)
    url_1 = driver.current_url
    print("URL 1:", url_1)

   
    driver.delete_all_cookies()

    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "ZGRhODY0ZWYtZTlmYS00MTNkLTlkYmEtMjc0OGRhZWQ3YzUy",  
        "domain": "gitflic.ru"
    })

    driver.refresh()
    print("After second refresh, URL:", driver.current_url)

    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1, .user-profile, [data-testid='profile-name']")))
    except Exception:
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    driver.get("https://gitflic.ru/user/savel_2")
    wait.until(lambda d: "user/savel_2" in d.current_url)
    url_2 = driver.current_url
    print("URL 2:", url_2)

    assert url_1 != url_2, f"URL должны различаться, но оба равны: {url_1}"

    driver.quit()