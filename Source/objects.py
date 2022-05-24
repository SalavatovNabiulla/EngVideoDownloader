import requests
import os
import progress
from bs4 import BeautifulSoup
import asyncio
import regex

class series:

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
        #
        self.set_source(url)
        self.set_seasons()

class season:

    def set_episodes(self):
        episodes = self.source.find("ul").find_all("li")
        for index in range(len(episodes)):
            self.episodes.append(episode(index+1,self.number,episodes[index]))

    def __init__(self,number,source):
        self.number = number
        self.source = source
        self.episodes = []
        #
        self.set_episodes()

class episode:

    def download(self):
        pass

    def set_video_link(self):
        result = requests.get(self.data_link)
        status_code = result.status_code
        # TODO: Сделать проверку доступности сайта, получая код ответа
        soup = BeautifulSoup(result.text, 'lxml')
        script = soup.find("script")
        pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
        self.video_link = str(pattern.findall(script.text)[4])


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