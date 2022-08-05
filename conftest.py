import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'  # Don't wait for the page to load fully
    # options.add_argument('headless')
    options.add_argument('--disable-blink-features')
    options.add_argument('--disable-extensions')
    options.add_argument('--incognito')
    options.add_argument('--disable-plugins-discovery')
    options.add_argument('--start-maximized')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
    )
    browser.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": "const newProto = navigator.__proto__ delete newProto.webdriver navigator.__proto__ = newProto"}
    )

    yield browser
    print("\nquit browser..")
    browser.quit()