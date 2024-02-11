from selenium import webdriver
import pytest

# Фикстура фин
# После завершения теста, который вызывал фикстуру,
# выполнение фикстуры продолжится со строки,которая следует за строкой со словом yield
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("C:\Users\Azerty\Desktop\Skillfactory\tests\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()