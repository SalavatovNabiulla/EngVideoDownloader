#--Imports
import time

import requests
import regex
import os
from threading import Thread
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#--SystemInterface
class series:

    # TODO: Добавить функции для загрузки всех сезонов

    def __set_seasons(self):
        soup = BeautifulSoup(self.source,"lxml")
        seasons = soup.find("div",class_="tab-content").find_all("div",class_="tab-pane")
        for index in range(len(seasons)):
            self.seasons.append(season(index+1,seasons[index],self))

    def __set_source(self,url):
        result = requests.get(url)
        status_code = result.status_code
        # TODO: Сделать проверку доступности сайта, получая код ответа
        self.source = result.text

    def __init__(self,url):
        self.seasons = []
        self.source = None
        self.cookie = None
        # TODO: Добавить информация о сеансе и Cookie
        #
        self.__set_source(url)
        self.__set_seasons()
#--
class season:

    #TODO: Добавить функции для загрузки всех серий

    def __set_episodes(self):
        episodes = self.source.find("ul").find_all("li")
        for index in range(len(episodes)):
            self.episodes.append(episode(index+1,self,episodes[index]))

    def __init__(self,number,source,series):
        print("Сбор информации о сезоне номер "+str(number))
        #--Variables
        self.number = number
        self.source = source
        self.episodes = []
        self.series = series
        #--Functions
        self.__set_episodes()
#--
class episode:

    def download(self,path):
        print("Начало загрузки серии № "+str(self.number)+" сезона № "+str(self.season.number))
        headers = {
            'Accept': 'video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5',
            'Accept-Language': 'en-US,ru-RU;q=0.8,ru;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            'Host': str(urlparse(self.video_link).netloc),
            'Origin': 'https://engvideo.pro',
            'Range': 'bytes=0-',
            'Referer': 'https://engvideo.pro/',
            'Sec-Fetch-Dest': 'video',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
        }
        result = requests.get(self.video_link, headers=headers, stream=True)
        status_code = result.status_code
        # TODO: Добавить обработку ошибки загрузки
        if status_code in (200,206):
            self.size = int(result.headers['Content-Length'])
            file_name = "S_" + str(self.season.number) + "_E_" + str(self.number) + ".mp4"
            with open(path + file_name, "wb") as file:
                chunk_size = 256
                for chunk in result.iter_content(chunk_size=chunk_size):
                    self.download_size = self.download_size + chunk_size;
                    file.write(chunk)
                self.downloaded = True
        else:
            print("Ошибка загрузки серии (Код ошибки: "+str(status_code)+")")
            self.downloaded = True

    def __set_video_link(self):
        result = requests.get(self.data_link)
        status_code = result.status_code
        # TODO: Сделать проверку доступности сайта, получая код ответа
        soup = BeautifulSoup(result.text, 'lxml')
        script = soup.find("script")
        pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
        spl = str(pattern.findall(script.text)[4]).replace("{","").replace("}","").replace(" ","").replace('"',"").replace(",","").split(":")
        self.video_link = spl[1]+":"+spl[2]
        path = "C:\\Users\\snmsu\\Desktop\\Test\\"
        with open(path+"temp.txt","w") as file:
            file.write(self.video_link)
        with open(path + "temp.txt", "r") as file:
            test = file.read().splitlines()
            self.video_link = test[0]
        os.remove(path+"temp.txt")

    def __set_data_link(self):
        self.data_link = self.data_link + self.source.find("div", class_="clearfix").find("div", class_="pull-left").find("h5", class_="margin_b5").find("a")["data-href"]

    def __init__(self,number,season,source):
        self.number = number
        self.season = season
        self.source = source
        self.data_link = 'https://engvideo.pro'
        self.video_link = ''
        self.size = 0
        self.download_size = 0
        self.downloaded = False
        #
        self.__set_data_link()
        self.__set_video_link()
        # TODO: Добавить определение названия серии
#--
class download_manager:


    def __start_downloading(self):
        for episode in self.queue:
            self.current_task = episode
            episode.download(self.path)
        self.complete = True

    def __init__(self,queue,path):
        self.path = path
        self.queue = queue
        self.thread = Thread(target=self.__start_downloading,args=([]))
        self.complete = False
        self.current_task = None
        #
        self.thread.start()

#--UserInterface

url = "https://engvideo.pro/ru/serials/family-guy/"
path = "C:\\Users\\snmsu\\Desktop\\Test\\"
series = series(url)
#TODO: Доделать Download manager
queue = [series.seasons[0].episodes[0]]
downloader = download_manager(queue,path)
while downloader.complete == False:
    os.system("cls")
    print("---")
    print("Season number: " + str(downloader.current_task.season.number))
    print("Series number: "+str(downloader.current_task.number))
    print("Total size: "+str(downloader.current_task.size/1000000)+" MB")
    print("Downloaded size: "+str(downloader.current_task.download_size/1000000)+" MB")
    print("---")
    time.sleep(1)
#--AnotherTODOes
#TODO: Добавить интерфейс(Консольный или графический)
#TODO: Добавить возможность устанавливать прокси на случай если сериал в стране заблокирован
#TODO: Добавить скорость загрузки