import pytest
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.home_page import HomePage


@pytest.mark.parametrize("home_url", [("http://htmlbook.ru/")])
class TestHomePage():

    def test_logo_directs_on_home_page(self, browser, home_url):
        page = HomePage(browser, home_url)
        page.open()
        time.sleep(4)
        page.click_on_logo()
        time.sleep(4)
        page.logo_click_should_direct_on_home_page(home_url)

    @pytest.mark.parametrize(
        "topmenu_category_xpath, topmenu_option_xpath, topmenu_option_success_url",
        [
            ('//a[@href="#main"]', '//header//a[text()="Статьи"]', 'http://htmlbook.ru/content'),
            ('//a[@href="#main"]', '//header//a[text()="Блог"]', 'http://htmlbook.ru/blog'),
            ('//a[@href="#main"]', '//header//a[text()="Практикум"]', 'http://htmlbook.ru/practical'),
            ('//a[@href="#main"]', '//header//a[text()="Форум"]', 'https://htmlforum.io/'),
            ('//a[@href="#html"]', '//header//a[text()="Самоучитель HTML"]', 'http://htmlbook.ru/samhtml'),
            ('//a[@href="#html"]', '//header//a[text()="Справочник по HTML"]', 'http://htmlbook.ru/html'),
            ('//a[@href="#html"]', '//header//a[text()="XHTML"]', 'http://htmlbook.ru/xhtml'),
            ('//a[@href="#html"]', '//header//a[text()="HTML5"]', 'http://htmlbook.ru/html5'),
            ('//a[@href="#css"]', '//header//a[text()="Самоучитель CSS"]', 'http://htmlbook.ru/samcss'),
            ('//a[@href="#css"]', '//header//a[text()="Справочник по CSS"]', 'http://htmlbook.ru/css'),
            ('//a[@href="#css"]', '//header//a[text()="Рецепты CSS"]', 'http://htmlbook.ru/faq'),
            ('//a[@href="#css"]', '//header//a[text()="CSS3"]', 'http://htmlbook.ru/css3'),
            ('//a[@href="#site"]', '//header//a[text()="Вёрстка веб-страниц"]', 'http://htmlbook.ru/samlayout'),
            ('//a[@href="#site"]', '//header//a[text()="Макеты"]', 'http://htmlbook.ru/layout'),
            ('//a[@href="#site"]', '//header//a[text()="Веб-сервер"]', 'http://htmlbook.ru/webserver'),
        ]
    )
    def test_topmenu_option_is_avalible_and_directs_on_correct_page(self, browser, home_url,
        topmenu_category_xpath, topmenu_option_xpath, topmenu_option_success_url):
        page = HomePage(browser, home_url)
        page.open()
        page.click_on_topmenu_category(topmenu_category_xpath)
        page.click_on_topmenu_option(topmenu_option_xpath)
        page.wait_until_home_url_changes(home_url)
        page.topmenu_option_should_direct_on_correct_page(topmenu_option_success_url)
    
    def test_header_search_field_is_on_home_page(self, browser, home_url):
        page = HomePage(browser, home_url)
        page.open()
        page.header_search_field_should_be_on_home_page()
    
    @pytest.mark.parametrize("correct_placeholder", [("Поиск по сайту")])
    def test_header_search_field_has_correct_placeholder(self, browser, home_url, correct_placeholder):
        page = HomePage(browser, home_url)
        page.open()
        page.header_search_field_should_have_correct_placeholder(correct_placeholder)

    def test_header_search_button_is_avalible(self, browser, home_url):
        page = HomePage(browser, home_url)
        page.open()
        page.click_on_header_search_button()

    @pytest.mark.parametrize("success_url", [('http://htmlbook.ru/search')])
    def test_header_search_button_directs_on_correct_page(self, browser, home_url, success_url):
        page = HomePage(browser, home_url)
        page.open()
        page.click_on_header_search_button()
        page.header_search_button_should_direct_on_correct_page(success_url, home_url)