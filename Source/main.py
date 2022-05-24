import objects
import requests
import os
import progress
from bs4 import BeautifulSoup
import asyncio

url = "https://engvideo.pro/ru/serials/family-guy/"
series = objects.series(url)
print(series.seasons[0].episodes[0].video_link)