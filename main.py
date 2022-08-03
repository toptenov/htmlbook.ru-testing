from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://htmlbook.ru/"

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
browser = webdriver.Chrome(options=options)
browser.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
)
browser.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {"source": "const newProto = navigator.__proto__ delete newProto.webdriver navigator.__proto__ = newProto"}
)

try:
    browser.get(link)
    time.sleep(3)
    button = browser.find_element(By.XPATH, '//a[@href="/content"]')
    button.click()
    time.sleep(3)
finally:
    browser.quit()
