#Imports
import asyncio

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
import subprocess
import os

#Public variables
links = []
tasks = []
loop = asyncio.new_event_loop()

#Parsing functions
async def process_current_season(index):
    # TODO: Добавить прогресс обработки сезона
    driver = create_driver()
    driver = set_current_season(driver, index)
    print("Начало обработки сезона "+str(index+1))
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
        print("Конец обработки сезона " + str(index+1))
    except Exception as ex:
        print("Ошибка обработки сезона "+str(index+1))
    finally:
        driver.close()
def process_all_seasons():
    for index in range(get_seasons_count()):
        tasks.append(loop.create_task(process_current_season(index)))
        #process_current_season(driver)
def get_seasons_count():
    driver = create_driver()
    driver.get(url)
    seasons_count = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div[5]/div[2]/div[3]/div[1]/ul").find_elements(By.TAG_NAME, "li")
    driver.close()
    return len(seasons_count)
def set_current_season(driver,index):
    driver.get(url)
    seasons = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div[5]/div[2]/div[3]/div[1]/ul").find_elements(By.TAG_NAME, "li")
    seasons[index].click()
    return driver
def start_parsing():
    try:
        process_all_seasons()
    except Exception as ex:
        print(ex)

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
    os.environ['WDM_LOG_LEVEL'] = '0'
    service = Service(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.headless = True
    options.add_argument("--mute-audio")
    options.add_argument("--disable-blink-features")
    driver = webdriver.Firefox(service=service,options=options)
    return driver

#Main
url = input("Введите ссылку на сериал: ")
path_to_exe = "C:\\Program Files (x86)\\Download Master\\dmaster.exe"
start_parsing()
wait = asyncio.wait(tasks)
loop.run_until_complete(wait)
start_video_downloading()
