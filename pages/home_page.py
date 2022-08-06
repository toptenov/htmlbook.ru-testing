from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    def click_on_logo(self):
        self.click_on_element(By.CSS_SELECTOR, ".logo")

    def logo_click_should_direct_on_home_page(self, home_url):
        url = self.browser.current_url
        assert url == home_url, f"Url of the logo is {url} istead of {home_url}"

    def click_on_topmenu_category(self, topmenu_category_xpath):
        self.click_on_element(By.XPATH, topmenu_category_xpath)

    def click_on_topmenu_option(self, topmenu_option_xpath):
        self.click_on_element(By.XPATH, topmenu_option_xpath)

    def wait_until_home_url_changes(self, home_url):
        self.wait_until_URL_be_changed(home_url)

    def topmenu_option_should_direct_on_correct_page(self, topmenu_option_success_url):
        current_url = self.browser.current_url
        assert current_url == topmenu_option_success_url,\
            f"Url of the article page is {current_url} istead of {topmenu_option_success_url}"

    def header_search_field_should_be_on_home_page(self):
        assert self.is_element_presented(By.CSS_SELECTOR, 'header input#q'), "Search field is not on home page"

    def header_search_field_should_have_correct_placeholder(self, correct_placeholder):
        current_placeholder = self.get_element(By.CSS_SELECTOR, 'header input#q').get_attribute('placeholder')
        assert current_placeholder == correct_placeholder,\
            f"Placeholder of header search field is {current_placeholder} instead of {correct_placeholder}"

    def click_on_header_search_button(self):
        self.click_on_element(By.CSS_SELECTOR, 'header input.find')

    def header_search_button_should_direct_on_correct_page(self, success_url, home_url):
        self.wait_until_URL_be_changed(home_url)
        url = self.browser.current_url
        assert success_url in url, f"Url {url} doesn't contain {success_url}"