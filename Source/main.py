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

    def __show_progress(self):
        while self.complete == False:
            os.system('cls')
            print('Сбор информации')
            print('---------------')
            for season in self.seasons:
                print('Сезон номер '+str(season.number)+' - Количество серий - '+str(len(season.episodes)))
            print('---------------')
            time.sleep(2)
        if self.complete:
            os.system('cls')
            print('Сбор информации')
            print('---------------')
            for season in self.seasons:
                print('Сезон номер '+str(season.number)+' - Количество серий - '+str(len(season.episodes)))
            print('---------------')
            set_queue(path,self)

    def __set_seasons(self):
        soup = BeautifulSoup(self.source,"lxml")
        seasons = soup.find("div",class_="tab-content").find_all("div",class_="tab-pane")
        for index in range(len(seasons)):
            self.seasons.append(season(index+1,seasons[index],self))
        self.complete = True

    def __set_source(self,url):
        session = requests.Session()
        result = session.get(url)
        status_code = result.status_code
        if status_code == 200:
            self.source = result.text
            self.session = session
            Thread(target=self.__show_progress, args=([])).start()
            self.__set_seasons()
        else:
            print("Ошибка подключения к сайту. (Код ошибки: "+str(status_code)+")")

    def __init__(self,url,path):
        self.seasons = []
        self.source = None
        self.cookie = None
        self.complete = False
        self.path = path
        self.session = None
        self.__set_source(url)
#--
class season:

    def __set_episodes(self):
        episodes = self.source.find("ul").find_all("li")
        for index in range(len(episodes)):
            self.episodes.append(episode(index+1,self,episodes[index]))
        # print("Количество серий: "+str(len(self.episodes)))

    def __init__(self,number,source,series):
        # print("Сбор информации о сезоне номер "+str(number))
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
        result = self.season.series.session.get(self.video_link, headers=headers, stream=True)
        status_code = result.status_code
        if status_code in (200,206):
            self.size = int(result.headers['Content-Length'])
            file_name = "S_" + str(self.season.number) + "_E_" + str(self.number) + ".mp4"
            #
            with open(path + file_name, "wb") as file:
                chunk_size = 256
                for chunk in result.iter_content(chunk_size=chunk_size):
                    self.download_size = self.download_size + chunk_size;
                    file.write(chunk)
                    # print("Загружено: "+str(round(self.download_size/1000000))+"/"+str(round(self.size/1000000))+" MB")
                self.good_download = True
            # print("Завершение загрузки эпизода номер "+str(episode.number)+" сезона номер "+str(episode.season.number))
        else:
            # print("Ошибка загрузки серии (Код ошибки: "+str(status_code)+")")
            self.bad_download = True

    def __set_video_link(self):
        result = self.season.series.session.get(self.data_link)
        status_code = result.status_code
        if status_code == 200:
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
        self.good_download = False
        self.bad_download = False
        #
        self.__set_data_link()
        self.__set_video_link()
#--
class download_manager:


    def __show_progress(self):
        while self.complete == False:
            os.system('cls')
            print("Очередь загрузки:")
            print("-----------------")
            for episode in self.queue:
                if (episode.good_download == False) and (episode.bad_download == False):
                    print("Серия номер "+str(episode.number)+" сезона номер "+str(episode.season.number)+" : "+str(round(episode.download_size/1000000))+"/"+str(round(episode.size/1000000))+" MB")
            print("-----------------")
            time.sleep(1)
            complete = True
            for episode in self.queue:
                if (episode.good_download == False) and (episode.bad_download == False):
                    complete = False
            self.complete = complete
        #
        os.system('cls')
        print("-----------------")
        print("Загрузка завершена!")
        print("-----------------")

    def __start_downloading(self):
        for episode in self.queue:
            # print("Начало загрузки эпизода номер "+str(episode.number)+" сезона номер "+str(episode.season.number))
            self.current_task = episode
            Thread(target=episode.download,args=([self.path])).start()

    def __init__(self,queue,path):
        self.path = path
        self.queue = queue
        self.complete = False
        self.current_task = None
        #
        Thread(target=self.__show_progress,args=([])).start()
        Thread(target=self.__start_downloading, args=([])).start()
#--
def set_queue(path,series):
    ask = input('''Выберите действие:
    1) Загрузить сериал целиком
    2) Загрузить определенные сезоны целиком 
    :''')
    queue = []
    if ask == "1":
        for season in series.seasons:
            for episode in season.episodes:
                queue.append(episode)
        downloader = download_manager(queue, path)
    elif ask == "2":
        seasons = input('Введите номера сезонов через запятую: ').split(',')
        for season in seasons:
            for episode in series.seasons[int(season) - 1].episodes:
                queue.append(episode)
        downloader = download_manager(queue, path)
    else:
        print("Ошибка выбора действия")

#--UserInterface
url = input("Введите ссылку на сериал: ")
path = input("Введите папку загрузки: ")
if path[len(path)-1] != "\\":
    path = path+"\\"
if os.path.isdir(path):
    series = series(url,path)
else:
    print("Нет доступа к указанному каталогу")