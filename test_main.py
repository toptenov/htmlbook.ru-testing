import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("home_url, timeout", [("http://htmlbook.ru/", 10)])
class TestHomePage():
    def test_logo_directs_to_home_page(self, browser, home_url, timeout):
        browser.get(home_url)
        time.sleep(4)
        logo = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".logo"))
        )
        logo.click()
        time.sleep(4)
        url = browser.current_url
        assert url == home_url, f"Url of the logo is {url} istead of {home_url}"
       
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
    def test_topmenu_is_avalible_and_directs_to_correct_links(
        self, browser, home_url, timeout,
        topmenu_category_xpath, topmenu_option_xpath, topmenu_option_success_url):

        browser.get(home_url)
        topmenu_category = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.XPATH, topmenu_category_xpath))
        )
        topmenu_category.click()
        topmenu_option = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.XPATH, topmenu_option_xpath))
        )
        topmenu_option.click()
        WebDriverWait(browser, timeout).until(
            EC.url_changes(home_url)
        )
        url = browser.current_url
        assert \
            url == topmenu_option_success_url,\
            f"Url of the article page is {url} istead of {topmenu_option_success_url}"

    @pytest.mark.parametrize("correct_placeholder", [("Поиск по сайту")])
    def test_header_search_field_is_avalible(
        self, browser, home_url, timeout, correct_placeholder):

        browser.get(home_url)
        header_search_field = WebDriverWait(browser, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header input#q'))
        )
        placeholder = header_search_field.get_attribute('placeholder')
        assert placeholder == correct_placeholder,\
            f"Placeholder of header search field is {placeholder} instead of {correct_placeholder}"
    
    @pytest.mark.parametrize("success_url",
        [
            ('http://htmlbook.ru/search')
        ]
    )
    def test_header_search_button_is_avalible(
        self, browser, home_url, timeout, success_url):

        browser.get(home_url)
        header_search_button = WebDriverWait(browser, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header input.find'))
        )
        header_search_button.click()
        WebDriverWait(browser, timeout).until(
            EC.url_changes(home_url)
        )
        url = browser.current_url
        assert success_url in url, f"Url {url} doesn't contain {success_url}"

if __name__ == "__main__":
    TestHomePage.test_articles_button_is_avalible_on_home_page()
    print("All tests passed!")
