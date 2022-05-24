#--Imports
import requests
from bs4 import BeautifulSoup
import regex

#--SystemInterface
class series:

    # TODO: Добавить функции для загрузки всех сезонов

    def set_seasons(self):
        soup = BeautifulSoup(self.source,"lxml")
        seasons = soup.find("div",class_="tab-content").find_all("div",class_="tab-pane")
        for index in range(len(seasons)):
            self.seasons.append(season(index+1,seasons[index]))

    def set_source(self,url):
        result = requests.get(url)
        status_code = result.status_code
        # TODO: Сделать проверку доступности сайта, получая код ответа
        self.source = result.text
        #

    def __init__(self,url):
        self.seasons = []
        self.source = None
        # TODO: Добавить информация о сеансе и Cookie
        #
        self.set_source(url)
        self.set_seasons()
#--
class season:

    #TODO: Добавить функции для загрузки всех серий

    def set_episodes(self):
        episodes = self.source.find("ul").find_all("li")
        for index in range(len(episodes)):
            self.episodes.append(episode(index+1,self,episodes[index]))

    def __init__(self,number,source):
        print("Сбор информации о сезоне номер "+str(number))
        self.number = number
        self.source = source
        self.episodes = []
        #
        self.set_episodes()
#--
class episode:

    def download(self,path):
        print("Начало загрузки серии № "+str(self.number)+" сезона № "+str(self.season.number))
        chunk_size = 256
        headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,ru-RU;q=0.8,ru;q=0.5,en;q=0.3",
            "Connection": "keep-alive",
            "Host": "media.ling.online",
            "Origin": "https://engvideo.pro",
            "Range": "bytes=0-",
            "Referer": "https://engvideo.pro/",
            "Sec-Fetch-Dest": "video",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Download Master"
        }
        result = requests.get(self.video_link,stream=True,headers=headers)
        # TODO: Вес контента содержится в заголовке ответа "Content-Length". На основании этого можно сделать прогресс загрузки
        status_code = result.status_code
        # TODO: Добавить обработку ошибки загрузки
        if status_code == 200:
            file_name = "S_"+str(self.season.number)+"_E_"+str(self.number)+".mp4"
            with open(path+file_name,"wb") as file:
                for chunk in result.iter_content(chunk_size=chunk_size):
                    file.write(chunk)
            print("Конец загрузки серии № " + str(self.number) + " сезона № " + str(self.season.number))
        else:
            print("Ошибка загрузки серии (Код ошибки: "+str(status_code)+")")

    def set_video_link(self):
        result = requests.get(self.data_link)
        status_code = result.status_code
        # TODO: Сделать проверку доступности сайта, получая код ответа
        soup = BeautifulSoup(result.text, 'lxml')
        script = soup.find("script")
        pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
        spl = video_link = str(pattern.findall(script.text)[4]).replace("{","").replace("}","").replace(" ","").replace('"',"").replace(",","").split(":")
        self.video_link = spl[1]+":"+spl[2]

    def set_data_link(self):
        self.data_link = self.data_link + self.source.find("div", class_="clearfix").find("div", class_="pull-left").find("h5", class_="margin_b5").find("a")["data-href"]

    def __init__(self,number,season,source):
        self.number = number
        self.season = season
        self.source = source
        self.data_link = 'https://engvideo.pro'
        self.video_link = ''
        #
        self.set_data_link()
        self.set_video_link()
        # TODO: Добавить определение названия серии

#--UserInterface
url = "https://engvideo.pro/ru/serials/chernobyl/"
path = "C:\\Users\\snmsu\\Desktop\\Test\\"
series = series(url)
series.seasons[0].episodes[0].download(path)

#--AnotherTODOes
#TODO: Добавить интерфейс(Консольный или графический)
#TODO: Добавить возможность устанавливать прокси на случай если сериал в стране заблокирован