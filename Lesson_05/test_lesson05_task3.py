from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://httpbin.qa-territory.online/links/10")
    sleep(2)

    links = driver.find_elements(By.TAG_NAME, "a")

    assert len(links) == 9, "Ошибка: количество ссылок не соответствует требуемому."
   
    for i, link in enumerate(links):
        assert link.is_displayed(), f"Ошибка: ссылка под индексом {i} не отображается на странице."

    # Самое важное: берём текст именно у первого элемента списка (индекс 0)
    first_link_text = links[0].text
    assert "1" in first_link_text, "Ошибка: текст первой ссылки не содержит '1'."
   

except Exception as e:
    print(f"X Произошла ошибка: {e}")
finally:
    driver.quit()
    