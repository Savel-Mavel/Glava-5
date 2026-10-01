import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def chrome_driver():
    """Фикстура для Chrome драйвера"""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    """Фикстура для Firefox драйвера (без обращения к GitHub API)"""
    # Путь к уже скачанному geckodriver
    gecko_path = r"C:\Users\User\.cache\selenium\geckodriver\win64\0.37.1\geckodriver.exe"
    
    # Если файла нет по этому пути, ищем в .wdm
    if not os.path.exists(gecko_path):
        wdm_path = os.path.expanduser(r"~\.wdm\drivers\geckodriver")
        for root, dirs, files in os.walk(wdm_path):
            if "geckodriver.exe" in files:
                gecko_path = os.path.join(root, "geckodriver.exe")
                break
    
    service = FirefoxService(gecko_path)
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()