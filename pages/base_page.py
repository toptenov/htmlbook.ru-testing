from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
    
    def open(self):
        self.browser.get(self.url)

    def is_element_presented(self, how_to_find, what_to_find):
        try:
            WebDriverWait(self.browser, self.timeout).until(
                EC.visibility_of_element_located((how_to_find, what_to_find))
            )
        except Exception as e:
            return False
        return True
    
    def get_element(self, how_to_find, what_to_find):
        assert self.is_element_presented(how_to_find, what_to_find), f"Element {what_to_find} is not on the page."
        return WebDriverWait(self.browser, self.timeout).until(
            EC.presence_of_element_located((how_to_find, what_to_find))
        )

    def click_on_element(self, how_to_find, what_to_find):
        assert self.is_element_presented(how_to_find, what_to_find), f"Element {what_to_find} is not on the page."
        element = WebDriverWait(self.browser, self.timeout).until(
            EC.element_to_be_clickable((how_to_find, what_to_find))
        )
        element.click()