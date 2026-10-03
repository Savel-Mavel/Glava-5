import allure
from allure_commons.types import Severity
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин SauceDemo")
@allure.story("Оформление заказа")
@allure.title("Проверка итоговой суммы трёх товаров в корзине")
@allure.description("""
    Тест проверяет корректность итоговой стоимости заказа.
    1. Авторизация как standard_user
    2. Добавление трёх товаров в корзину
    3. Оформление заказа с заполнением формы
    4. Проверка, что итоговая сумма равна $58.29
""")
@allure.severity(Severity.NORMAL)
def test_shop_checkout_total(firefox_driver):
    
    with allure.step("Авторизация на сайте"):
        login_page = LoginPage(firefox_driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
    
    with allure.step("Добавление товаров в корзину"):
        inventory = InventoryPage(firefox_driver)
        
        with allure.step("Добавить Sauce Labs Backpack"):
            inventory.add_product_by_name("Sauce Labs Backpack")
        
        with allure.step("Добавить Sauce Labs Bolt T-Shirt"):
            inventory.add_product_by_name("Sauce Labs Bolt T-Shirt")
        
        with allure.step("Добавить Sauce Labs Onesie"):
            inventory.add_product_by_name("Sauce Labs Onesie")
    
    with allure.step("Переход в корзину"):
        inventory.go_to_cart()
    
    with allure.step("Нажать кнопку Checkout"):
        cart = CartPage(firefox_driver)
        cart.go_to_checkout()
    
    with allure.step("Заполнение формы оформления заказа"):
        checkout = CheckoutPage(firefox_driver)
        checkout.fill_form("Михаил", "Савельев", "662606")
    
    with allure.step("Получение итоговой суммы"):
        total_text = checkout.get_total()
    
    with allure.step(f"Проверка, что итоговая сумма = $58.29 (фактически: {total_text})"):
        assert "$58.29" in total_text, f"Ожидалась сумма $58.29, получено {total_text}"