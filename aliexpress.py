from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service('./chromedriver')
options = Options()
options.add_argument('start-maximized')
options.add_experimental_option('excludeSwitches', ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)



driver = webdriver.Chrome(service=s, options=options)
driver.get('https://aliexpress.ru')

driver.implicitly_wait(10)

# search = driver.find_element(By.XPATH, "//input[@type='text']")
# search.send_keys("видеокарта")
# search.send_keys(Keys.ENTER)

for i in range(7):
    goods = driver.find_elements(By.XPATH, "//div[@data-product-id]")
    actions = ActionChains(driver)
    actions.move_to_element(goods[-1])
    actions.perform()

pages = 3
while pages > 0:
    # buttons_pagination = driver.find_elements(By.XPATH, "//a[contains(@class,'Pagination')]")
    # button_next = buttons_pagination[-1]
    # button_next.click()

    wait = WebDriverWait(driver, 10)
    next_button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    # next_button = driver.find_element(By.TAG_NAME, "button")
    next_button.click()
    pages -= 1

goods = driver.find_elements(By.XPATH, "//div[@data-product-id]")

for good in goods:
    name = good.find_element(By.XPATH, ".//div[@class='product-snippet_ProductSnippet__name__lido9p']").text
    price = good.find_element(By.XPATH, ".//div[@class='snow-price_SnowPrice__mainM__18x8np']").text
    print(name, price)


print()
