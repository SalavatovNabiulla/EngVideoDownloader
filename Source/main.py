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


    def __set_seasons(self):
        soup = BeautifulSoup(self.source,"lxml")
        seasons = soup.find("div",class_="tab-content").find_all("div",class_="tab-pane")
        for index in range(len(seasons)):
            self.seasons.append(season(index+1,seasons[index],self))
        self.complete = True

    def __set_source(self,url):
        try:
            session = requests.Session()
            result = session.get(url)
            status_code = result.status_code
            if status_code == 200:
                self.source = result.text
                self.session = session
                self.status_code = status_code
                self.connection_status = True
                self.__set_seasons()
            else:
                self.status_code = status_code
                self.connection_status = False
        except Exception as ex:
            self.connection_status = False
            print(ex)

    def __init__(self,url,path):
        self.seasons = []
        self.source = None
        self.cookie = None
        self.complete = False
        self.path = path
        self.session = None
        self.status_code = None
        self.connection_status = None
        self.__set_source(url)
#--
class season:

    def __set_episodes(self):
        episodes = self.source.find("ul").find_all("li")
        for index in range(len(episodes)):
            self.episodes.append(episode(index+1,self,episodes[index]))

    def __init__(self,number,source,series):
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
        self.__set_video_link()
        #
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
                self.good_download = True
        else:
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
            tmp_file = "temp_"+str(self.season.number)+"_"+str(self.number)+".txt"
            #TODO: Придумать вариант без временного файла (Костыль)
            with open(tmp_file,"w") as file:
                file.write(self.video_link)
            with open(tmp_file, "r") as file:
                test = file.read().splitlines()
                self.video_link = test[0]
            os.remove(tmp_file)

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
        # TODO: Добавить определение названия серии (Фича)
#--
class user_interface_cli:

    def __validate_path(self):

        if self.path[len(self.path) - 1] != "\\":
            self.path = self.path + "\\"
        self.path.replace('"',"")

    def __step_3(self):
        for episode in self.queue:
            #
            if os.path.isdir(self.path + str(episode.season.number)):
                season_path = self.path + str(episode.season.number) + "\\"
            else:
                os.mkdir(self.path + str(episode.season.number))
                season_path = self.path + str(episode.season.number) + "\\"
            #
            Thread(target=episode.download, args=([season_path])).start()
        #
        while self.download_complete == False:
            os.system('cls')
            print("Очередь загрузки:")
            print("-----------------")
            for episode in self.queue:
                if (episode.good_download == False) and (episode.bad_download == False):
                    print("Серия номер "+str(episode.number)+" сезона номер "+str(episode.season.number)+" : "+str(round(episode.download_size/1000000))+"/"+str(round(episode.size/1000000))+" MB")
            print("-----------------")
            time.sleep(1)
            download_complete = True
            for episode in self.queue:
                if (episode.good_download == False) and (episode.bad_download == False):
                    download_complete = False
            self.download_complete = download_complete
        #
        os.system('cls')
        print("-----------------")
        print("Загрузка завершена!")
        print("-----------------")

    def __step_2(self):
        os.system('cls')
        print(
        '''Выберите действие:
        1) Загрузить сериал целиком
        2) Загрузить определенные сезоны целиком
        3) Загрузить определенные серии определенного сезона''')
        choice = input(": ")
        if choice == "1":
            for season in self.series.seasons:
                for episode in season.episodes:
                    self.queue.append(episode)
            self.step = self.step + 1
        elif choice == "2":
            os.system('cls')
            seasons = input('Введите номера сезонов через запятую: ').split(',')
            for season in seasons:
                for episode in self.series.seasons[int(season) - 1].episodes:
                    self.queue.append(episode)
            self.step = self.step + 1
        elif choice == "3":
            os.system('cls')
            season_index = input('Введите номер сезона: ')
            try:
                os.system('cls')
                season = self.series.seasons[int(season_index)-1]
                episodes = input('Введите номера эпизодов через запятую: ').split(',')
                for episode_index in episodes:
                    try:
                        episode = season.episodes[int(episode_index)-1]
                        self.queue.append(episode)
                    except Exception as ex:
                        pass
                self.step = self.step + 1
            except Exception as ex:
                print("Сезон с таким номером не найден. Повторите попытку")
        else:
            print("Ошибка выбора действия. Повторите попытку")

    def __step_1(self):
        os.system('cls')
        self.series = series(self.url, self.path)
        if self.series.connection_status:
            self.step = self.step + 1
        elif self.series.connection_status == False:
            print("Не удалось получить доступ к сайту. Проверьте подключение к интернету, ссылку и повторите попытку")
            self.step = self.step - 1

    def __step_0(self):
        os.system('cls')
        self.url = input("Введите ссылку на сериал: ")
        #TODO: Добавить валидацию ссылки (Фича)
        if (self.path == None):
            self.path = input("Введите папку загрузки: ")
            self.__validate_path()
            if (os.path.isdir(self.path) == False):
                while (os.path.isdir(self.path) == False):
                    self.path = input("Введите папку загрузки: ")
                    self.__validate_path()
        self.step = self.step + 1

    def __start_interface(self):
        os.system('cls')
        while self.active:
            if (self.step == 0):
                self.__step_0()
            elif (self.step == 1):
                self.__step_1()
            elif (self.step == 2):
                self.__step_2()
            elif (self.step == 3):
                self.__step_3()
                self.active = False

    def __init__(self):
        self.series = None
        self.active = True
        self.url = None
        self.path = None
        self.step = 0
        self.queue = []
        self.download_complete = False
        #
        Thread(target=self.__start_interface,args=([])).start()

#--main

ui = user_interface_cli()

#--AnotherTODOes
#TODO: Добавить возможность устанавливать прокси на случай если сериал в стране заблокирован (Фича)
#TODO: Добавить скорость загрузки (Фича)