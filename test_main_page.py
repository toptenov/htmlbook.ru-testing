import pytest
import time

from pages.locators import HomePageLocators
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
            (
                HomePageLocators.TOPMENU_CATEGORY_MAIN,
                HomePageLocators.TOPMENU_OPTION_CONTENT,
                'http://htmlbook.ru/content'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_MAIN,
                HomePageLocators.TOPMENU_OPTION_BLOG,
                'http://htmlbook.ru/blog'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_MAIN,
                HomePageLocators.TOPMENU_OPTION_PRACTICAL,
                'http://htmlbook.ru/practical'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_MAIN,
                HomePageLocators.TOPMENU_OPTION_FORUM,
                'https://htmlforum.io/'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_HTML,
                HomePageLocators.TOPMENU_OPTION_SELF_INSTRUCTION_HTML_MANUAL,
                'http://htmlbook.ru/samhtml'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_HTML,
                HomePageLocators.TOPMENU_OPTION_HTML_GUIDE,
                'http://htmlbook.ru/html'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_HTML,
                HomePageLocators.TOPMENU_OPTION_XHTML,
                'http://htmlbook.ru/xhtml'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_HTML,
                HomePageLocators.TOPMENU_OPTION_HTML5,
                'http://htmlbook.ru/html5'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_CSS,
                HomePageLocators.TOPMENU_OPTION_SELF_INSTRUCTION_CSS_MANUAL,
                'http://htmlbook.ru/samcss'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_CSS,
                HomePageLocators.TOPMENU_OPTION_CSS_GUIDE,
                'http://htmlbook.ru/css'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_CSS,
                HomePageLocators.TOPMENU_OPTION_CSS_RECIPES,
                'http://htmlbook.ru/faq'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_CSS,
                HomePageLocators.TOPMENU_OPTION_CSS3,
                'http://htmlbook.ru/css3'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_SITE,
                HomePageLocators.TOPMENU_OPTION_WEB_LAYOUT,
                'http://htmlbook.ru/samlayout'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_SITE,
                HomePageLocators.TOPMENU_OPTION_LAYOUTS,
                'http://htmlbook.ru/layout'
            ),(
                HomePageLocators.TOPMENU_CATEGORY_SITE,
                HomePageLocators.TOPMENU_OPTION_WEBSERVER,
                'http://htmlbook.ru/webserver'
            ),
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
