from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def test_articles_button_is_avalible_on_home_page():
    home_url = "http://htmlbook.ru/"
    timeout = 5

    # Don't wait for the page to load fully:
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-extensions')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--start-maximized")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(desired_capabilities=caps, options=options)
    browser.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
    )
    browser.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": "const newProto = navigator.__proto__ delete newProto.webdriver navigator.__proto__ = newProto"}
    )

    try:
        browser.get(home_url)
        button = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/content"]'))
        )
        button.click()
        WebDriverWait(browser, timeout).until(
            EC.url_changes(home_url)
        )
        url = browser.current_url
        assert url == "http://htmlbook.ru/content", f"Url of the article page is {url} istead of http://htmlbook.ru/content"
    finally:
        browser.quit()

if __name__ == "__main__":
    test_articles_button_is_avalible_on_home_page()
    print("All tests passed!")
