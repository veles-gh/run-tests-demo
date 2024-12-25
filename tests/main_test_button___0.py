from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

import time


url = f"https://www.qa-practice.com/elements/button/simple"
options = Options()
options.add_argument('--headless')

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.maximize_window()


try:
    time.sleep(4)
    driver.get(url=url)

    # assert driver.find_element(By.ID, 'submit-id-submit').is_displayed()
    button_test = driver.find_element(By.ID, 'submit-id-submit').is_displayed()

    if button_test == True:
        print(button_test)
        print("Button found!!!")

    else:
        print(button_test)
        print("Button not found...")

except Exception as ex:
    print(ex)


finally:
    time.sleep(3)
    driver.close()
    driver.quit()



