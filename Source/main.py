#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
import subprocess
import os

#Public variables
links = []

#Parsing functions
def process_current_season(driver,tab):
    # TODO: Добавить прогресс обработки сезона
    driver.switch_to.window(tab)
    try:
        #TODO: Элемент с классом vjs-poster перекрывает элемент с тэгом li
        episodes = driver.find_element(By.CLASS_NAME, "tab-content").find_element(By.CLASS_NAME, "active").find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")
        for episode in episodes:
            try:
                #TODO: Обработка ошибки загрузки серии, чтобы загрузка продолжалась
                link = episode.find_element(By.CLASS_NAME, "margin_b5").find_element(By.TAG_NAME, "a")
                link.click()
                time.sleep(2)
                video_link = driver.find_element(By.ID, "lingonline-video_html5_api").get_attribute("src")
                video_close_button = driver.find_element(By.CLASS_NAME,"video-close-button")
                video_close_button.click()
                time.sleep(1)
                links.append(video_link)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
def process_all_seasons(driver):
    # TODO: Добавить асинхронную или многопоточную обработку (Чтобы каждый сезон в каждой вкладке обрабатывался отдельно)
    for tab in driver.window_handles:
        process_current_season(driver,tab)
def create_tabs_for_seasons(driver):
    try:
        driver.get(url)
        seasons_count = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div[5]/div[2]/div[3]/div[1]/ul").find_elements(By.TAG_NAME, "li")
        for index in range(len(seasons_count)):
            driver.switch_to.new_window('tab')
            driver.get(url)
            seasons = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div[5]/div[2]/div[3]/div[1]/ul").find_elements(By.TAG_NAME, "li")
            seasons[index].click()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
    except Exception as ex:
        pass
def start_parsing(driver):
    try:
        create_tabs_for_seasons(driver)
        process_all_seasons(driver)
    except Exception as ex:
        print(ex)
    finally:
        driver.quit()

#Downloading functions
def start_video_downloading():
    links_path = os.path.dirname(os.path.abspath(__file__))+'\\links.txt'
    try:
        os.remove(links_path)
    except Exception as ex:
        print(ex)
    with open('links.txt','w') as file:
        for link in links:
            file.write(link+"\n")
    subprocess.Popen([path_to_exe, links_path])

#Main functions
#TODO: Автоматическая установка приложения DownloadMaster из установщика или интернета
#TODO: Автоматическая установка библиотеки Selenium
def create_driver():
    service = Service(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.headless = False
    options.add_argument("--mute-audio")
    driver = webdriver.Firefox(service=service,options=options)
    return driver
def start_program():
    driver = create_driver()
    start_parsing(driver)
    start_video_downloading()

#Main
url = input("Введите ссылку на сериал: ")
path_to_exe = "C:\\Program Files (x86)\\Download Master\\dmaster.exe"
start_program()