## Задание

Автоматизировать приведенный ниже сценарий на Selenium c использованием любого совместимого языка программирования (какой удобнее), а также подготовить пользовательскую инструкцию для инженера, который будет запускать в дальнейшем эти тесты внутри своего окружения.

Сценарий для автоматизации:
1. Пользователь заходит на сайт Яндекс: www.yandex.ru
2. Вводит в поисковую строку фразу «расчет расстояний между городами» и запускает поиск
3. Среди результатов поиска пользователь ищет результат с сайта «avtodispetcher.ru»
4. Найдя нужный результат с этого сайта – пользовать кликает на данном результате и переходит на сайт www.avtodispetcher.ru/distance/ 
5. Убедившись, что открылась верная ссылка, пользователь вводит следующие значения в поля:
- Поле «Откуда» - «Тула»
- Поле «Куда» - «Санкт-Петербург»
- Поле «Расход топлива» - «9»
- Поле «Цена топлива» - «46»
6. Пользователь нажимает кнопку «Рассчитать» 
7. Пользователь проверяет что рассчитанное расстояние = 897 км, а стоимость топлива = 3726 руб.
8. Пользователь кликает на «Изменить маршрут»
9. В открывшейся форме в поле «Через города» вводит «Великий Новгород» 
10. Ждет минуту и снова нажимает «Рассчитать»
11. Пользователь проверяет что расстояние теперь = 966 км, а стоимость топлива = 4002 руб.

## Решение

Скринкаст запуска теста: https://yadi.sk/i/-PLfueGjBArVYg (2,3 Мб)

### Инструкция для запуска теста (MacOS)

1. Скачать и установить python 3: https://www.python.org/downloads/.

2. Установить selenium:

pip3 install selenium

3. Скачать и установить версию chromedriver, соответствующую версии браузера Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads. Добавить путь к chromedriver'у в PATH.

4. Скачать проект smartechQA_Mac. Распаковать, открыть файл test_distance.py и прописать путь к chromedriver'у, например:

driver = webdriver.Chrome('/Users/sereddos/selenium/chromedriver').

5. В консоли перейти в папку проекта и установить виртуальное окружение:

pip install pipenv

6. Установить pytest:

pipenv install pytest --dev

7. Запустить тест с помощью команды:

pipenv run python -m pytest

### Инструкция для запуска теста (Windows)

1. Скачать и установить python 3: https://www.python.org/downloads/. Добавить python в PATH.

2. Обновить менеджер пакетов pip:

python -m pip install --upgrade pip

3. Установить selenium:

pip3 install selenium

4. Скачать и установить версию chromedriver, соответствующую версии браузера Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads

5. Скачать проект smartechQA_Win. Распаковать, открыть файл test_distance.py и прописать путь к chromedriver'у, например:

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)

6. В консоли перейти в папку проекта и запустить тест с помощью команды:

python test_distance.py
