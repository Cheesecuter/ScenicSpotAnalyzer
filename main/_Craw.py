from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import threading
import time
import csv
import _FrozenDir
import _Database


class Craw:
    def __init__(self, db):
        self._db = db
        self._db = _Database.Database()
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
        }
        pass

    def _craw(self, url):
        req = requests.get(url, headers=self.headers)
        content = req.text
        soup = BeautifulSoup(content, 'lxml')
        return soup

    def _save(self):
        csvPath = self.srcPath+r'\\Cities.csv'
        Cname_list, Curl_list = self._crawCities()
        cities = pd.DataFrame({'Cname': Cname_list, 'Curl': Curl_list})
        cities.to_csv(csvPath, encoding='UTF_8_SIG', index=False)
        self._db._CitiesRowIT = 0
        self._db._Cname = []
        self._db._Curl = []
        self._db._CityData = []
        self.threadingList = []
        self.lock = threading.RLock()
        for i in range(0, len(Cname_list)):
            self.threadingList.append(i)
            self.threadingList[i] = threading.Thread(
                target=self._thread_attractions, args=(i, Cname_list, Curl_list,))
        for i in range(0, len(Cname_list)):
            self.threadingList[i].start()
            time.sleep(1)
        pass

    def _thread_attractions(self, i, Cname_list, Curl_list):
        self.lock.acquire(True)
        self._db._InitCitiesData(Cname_list[i], Curl_list[i])
        self._db._AttractionsRowIT = 0
        Cname_list2, Aname_list, AnameEn_list, Percentage_list = self._crawAttractions(
            Cname_list[i], Curl_list[i])
        self._db._Cname2 = []
        self._db._Aname = []
        self._db._AnameEn = []
        self._db._Percentage = []
        self._db._AttractionData = []
        for j in range(0, len(Aname_list)):
            self._db._InitAttractionsData(
                Cname_list2[j], Aname_list[j],  AnameEn_list[j], Percentage_list[j])
        self.lock.release()
        pass

    def _crawCities(self):
        url = 'http://travel.qunar.com/place/'
        soup = self._craw(url)
        self._Cname = []
        self._Curl = []
        sub_list = soup.find_all('div', attrs={'class': 'sub_list'})

        for i in range(0, len(sub_list)):
            attr = sub_list[i].find_all('a')
            for j in range(0, len(attr)):
                self._Cname.append(attr[j].text)
                self._Curl.append(attr[j].attrs['href'])
        return self._Cname, self._Curl

    def _crawAttractions(self, Cname, Curl):
        url = Curl+'-jingdian'
        _Cname = []
        _Aname = []
        _AnameEn = []
        _Percentage = []
        response = requests.get(url, headers=self.headers)
        csvPath = self.srcPath+r'\\Attractions.csv'
        pageContent = response.text
        pageContent.encode().decode
        obj = re.compile(
            r'.*?<li class="item"'
            r'.*?<div class="ct">'
            r'.*?<div class="titbox clrfix">'
            r'.*?<span class="cn_tit">(?P<Aname>.*?)<span class="en_tit">(?P<AnameEn>.*?)</span>'
            r'.*?<div class="txtbox clrfix">'
            r'.*?<span class="sum">(?P<Percentage>.*?)%</span>', re.S
        )
        result = obj.finditer(pageContent)
        for i in result:
            _Cname.append(Cname)
            _Aname.append(i.group("Aname"))
            _AnameEn.append(i.group("AnameEn"))
            _Percentage.append(i.group("Percentage"))
            pass
        return _Cname, _Aname, _AnameEn, _Percentage
