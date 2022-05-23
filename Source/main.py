#Imports
import json
import requests
import subprocess
import os
from bs4 import BeautifulSoup
import regex

#Public variables
video_links = []
media_links = []
data_links = []

#Parsing functions
def start_parsing_video_links():
    for m_link in media_links:
        page_path = os.path.dirname(os.path.abspath(__file__)) + '\\page.html'
        try:
            os.remove(page_path)
        except Exception as ex:
            pass
        res = requests.get(m_link)
        with open(page_path,'w', encoding="utf-8") as file:
            file.write(res.text)
        with open(page_path,'r', encoding="utf-8") as file:
            content = file.read()
            soup = BeautifulSoup(content,'lxml')
            script = soup.find("script")
            pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
            test = pattern.findall(script.text)
            link = str(test[4])
            try:
                os.remove("link.txt")
            except Exception as ex:
                pass
            with open("link.txt","w") as file:
                file.write(link)
            with open("link.txt","r") as file:
                lines = file.readlines()
                link = lines[1].split(":")
                link = link[1]+":"+link[2]
                link = link.replace(',','').replace('"','').replace(' ','')
                video_links.append(link)
def create_media_links():
    host = "https://engvideo.pro"
    for link in data_links:
        media_links.append(host+link)
def start_parsing():
    with open("main.html","r",encoding="utf-8") as file:
        content = file.read()
        soup = BeautifulSoup(content,"lxml")
        seasons = soup.find("div",class_="tab-content").find_all("div",class_="tab-pane")
        for season in seasons:
            episodes = season.find("ul").find_all("li")
            for episode in episodes:
                episode_href = episode.find("div",class_="clearfix").find("div",class_="pull-left").find("h5",class_="margin_b5").find("a")["data-href"]
                data_links.append(episode_href)

#Downloading functions
#TODO: Сортировка серий по папкам
def start_site_downloading():
    site_path = os.path.dirname(os.path.abspath(__file__)) + '\\main.html'
    try:
        os.remove(site_path)
    except Exception as ex:
        pass
    res = requests.get(url)
    with open(site_path,'w', encoding="utf-8") as file:
         file.write(res.text)
def start_video_downloading():
    path = os.path.dirname(os.path.abspath(__file__))+'\\links.txt'
    try:
        os.remove(path)
    except Exception as ex:
        print(ex)
    with open(path,'w') as file:
        for link in video_links:
            file.write(link+"\n")
    subprocess.Popen([path_to_exe, path])

#Main functions
#TODO: Автоматическая установка приложения DownloadMaster из установщика или интернета
#TODO: Автоматическая установка библиотеки Selenium

#Main
url = input("Введите ссылку на сериал: ")
path_to_exe = "C:\\Program Files (x86)\\Download Master\\dmaster.exe"
start_site_downloading()
start_parsing()
create_media_links()
start_parsing_video_links()
start_video_downloading()