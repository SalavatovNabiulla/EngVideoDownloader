from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
import subprocess
import os

url = "https://engvideo.pro/ru/serials/family-guy/"
#url = "https://engvideo.pro/ru/serials/chernobyl/"
path_to_exe = "C:\\Program Files (x86)\\Download Master\\dmaster.exe"
links = []

def start_driver():
    service = Service(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(service=service,options=options)
    try:
        driver.get(url)
        #time.sleep(2)
        seasons = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[5]/div[2]/div[3]/div[1]/ul").find_elements(By.TAG_NAME, "li")
        # TODO: Асинхронная обработка сезонов в отдельных вкладках, чтобы не ждать загрузку каждого файла
        for season in seasons:
            try:
                season.click()
                #TODO: Элемент с классом vjs-poster перекрывает элемент с тэгом li
                episodes = driver.find_element(By.CLASS_NAME, "tab-content").find_element(By.CLASS_NAME, "active").find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")
                for episode in episodes:
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
                print("Сезон "+season.text+" не был загружен")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def start_downloader():
    links_path = os.path.dirname(os.path.abspath(__file__))+'\\links.txt'
    try:
        os.remove(links_path)
    except:
        test = 0
    with open('links.txt','w') as file:
        for link in links:
            file.write(link+"\n")
    subprocess.Popen([path_to_exe, links_path])


#TODO: Добавить консольный интерфейс для ввода ссылки на сериал и т.д.
start_driver()
start_downloader()