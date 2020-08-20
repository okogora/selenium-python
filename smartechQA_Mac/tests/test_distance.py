#Импортируем модули
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    #Запускаем драйвер и браузер
    driver = webdriver.Chrome('/Users/sereddos/selenium/chromedriver')
    driver.get("http://www.google.com")

    #Возвращаем объект драйвера в конце установки
    yield driver

    #Закрываем драйвер, высвобождаем ресурсы
    driver.quit()

def test_yandex_search(driver):
    #Сохраняем URL страницы поиска и запрос в переменные
    URL = 'https://www.yandex.ru'
    PHRASE = 'расчет расстояний между городами'

    #Переходим на страницу поиска и ждём 10 сек.
    driver.get(URL)
    driver.implicitly_wait(10)

    #Ищем поле ввода запроса, вводим запрос и нажимаем Enter; ждём 10 сек.
    search_input = driver.find_element_by_id('text')
    search_input.send_keys(PHRASE + Keys.RETURN)
    driver.implicitly_wait(10)

    #Сохраняем в переменную первую вкладку (с результатами поиска)
    window_before = driver.window_handles[0]

    #Ищем часть текста ссылки на странице результатов поиска и нажимаем на ссылку
    search_result = driver.find_element_by_partial_link_text('avtodispetcher.ru').click()

    #Сохраняем в переменную вторую вкладку, которая открывается после клика по ссылке
    window_after = driver.window_handles[1]

    #Переходим на вторую вкладку
    driver.switch_to.window(window_after)

    #Убеждаемся, что открылась верная ссылка
    assert 'https://www.avtodispetcher.ru/distance/' in driver.current_url

    #Ищем и сохраняем в переменную поле "Откуда", вводим в поле значение "Тула"
    route_from = driver.find_element_by_name('from').send_keys('Тула')

    #Ищем и сохраняем в переменную поле "Куда", вводим в поле значение "Санкт-Петербург"
    route_to = driver.find_element_by_name('to').send_keys('Санкт-Петербург')

    #Ищем и сохраняем в переменную поле "Расход топлива"
    fuel_consumption = driver.find_element_by_name('fc')

    #Очищаем поле (удаляем плейсхолдер)
    fuel_consumption.clear()

    #Вводим в поле значение "9"
    fuel_consumption.send_keys("9")

    #Ищем и сохраняем в переменную поле "Цена топлива"
    fuel_price = driver.find_element_by_name('fp')

    #Очищаем поле (удаляем плейсхолдер)
    fuel_price.clear()

    #Вводим в поле значение "46"
    fuel_price.send_keys('46')

    #Ищем и сохраняем в переменную кнопку "Рассчитать", нажимаем на неё
    calculate_button = driver.find_element_by_css_selector('.submit_button > input[type="submit"]').send_keys(Keys.RETURN)

    #Ищем и сохраняем в переменную рассчитанное расстояние
    total_distance = driver.find_element_by_id('totalDistance')

    #Проверяем, что расстояние == 897 км
    assert '897' in total_distance.text

    #Ищем и сохраняем в переменную рассчитанную стоимость топлива; проверяем, что элемент содержит ожидаемое значение
    total_price = driver.find_elements_by_xpath("//*[contains(text(), '3726')]")
    driver.implicitly_wait(10)

    #Ищем, сохраняем в переменную и нажимаем на элемент "Настроить маршрут"
    change_route = driver.find_element_by_class_name('anchor').click()

    #Ищем и сохраняем в переменную поле "Через города", вводим в него значение "Великий Новгород"
    route_via = driver.find_element_by_name('v').send_keys('Великий Новгород')

    #Ждём 60 сек.
    driver.implicitly_wait(60)

    #Ищем и сохраняем в переменную кнопку "Рассчитать", нажимаем на неё
    new_calculate_button = driver.find_element_by_css_selector('.submit_button > input[type="submit"]').send_keys(Keys.RETURN)

    #Ищем и сохраняем в переменную рассчитанное расстояние
    new_total_distance = driver.find_element_by_id('totalDistance')

    #Проверяем, что новое расстояние == 966 км
    assert '966' in new_total_distance.text

    #Проверяем, что новая стоимость топлива == 4002 руб.
    new_total_price = driver.find_elements_by_xpath("//*[contains(text(), '4002')]")
