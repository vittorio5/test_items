from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_add_to_basket_button_exists(browser):
    # даём время на визуальный осмотр страницы
    time.sleep(30)
    # пытаемся найти на странице кнопку добавления в корзину
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))
        button_exists = True        
    except:
        button_exists = False        
    finally:
        # Проверяем, была ли найдена кнопка на странице
        assert button_exists, "Кнопка добавления в корзину отсутствует на странице!"
