from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import pyautogui


url = "https://engvideo.pro/ru/serials/family-guy/"
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get(url)
    time.sleep(5)

    #tab_bar = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[5]/div[2]/div[3]/div[1]/ul")
    #tab_items = tab_bar.find_elements(By.TAG_NAME, "li")
    #tab_items[0].click()
    #time.sleep(5)
    series_list = driver.find_element(By.CLASS_NAME, "tab-content")
    series_content = series_list.find_element(By.CLASS_NAME, "active")
    series_items_list = series_content.find_element(By.TAG_NAME, "ul")
    series_items = series_items_list.find_elements(By.TAG_NAME, "li")
    title = series_items[0].find_element(By.CLASS_NAME, "margin_b5")
    link = title.find_element(By.TAG_NAME,"a")
    link.click()
    time.sleep(5)
    video = driver.find_element(By.ID, "lingonline-video_html5_api")
    webdriver.ActionChains(driver).context_click(video).perform()
    time.sleep(5)
    for i in range(10):
        pyautogui.press("down")
        time.sleep(1)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
