# FinalHomework32.1 Тесты находятся в ветке MASTER
Финальный тестовый проект SkillFactory курса QAP-142

Автоматизированное тестирование UI сайта: с использованием PyTest и Selenium ( https://lk.rt.ru/  компании ООО «РТК ИТ»)

Тест-кейсы  по ссылке: https://docs.google.com/spreadsheets/d/1BvinBGPVQArSwJMOyacR1DEl3gdCj-wy/edit?usp=sharing&ouid=109499880344179079981&rtpof=true&sd=true

В папке pages в файле main_page.py находится конструктор webdriver и общие для всех тестируемых страниц методы.

В папке pages в файлах main_page.py, recovery_page.py, registration_page.py находятся методы для соответствующих тестируемых страниц.

В папке pages в файле "locators.py находятся все локаторы.

В корне проекта в файле conftest.py находится фикстура с функцией открытия и закрытия браузера. Для запуска тестов необходимо поменять путь до webdriver на свой.

В корне проекта в файлах test_main_page.py, test_recovery_page.py, test_registration_page.py находятся тесты. Все тесты идут по порядку в соответствии с номерами тест-кейсов. Во всех файлах с тестами находятся закомментированные команды для запуска тестов из командной строки (# pytest -v --tb=line test_main_page.py)
Необходимо установить все необходимые библиотеки pytest, selenium, pytest-selenium...
