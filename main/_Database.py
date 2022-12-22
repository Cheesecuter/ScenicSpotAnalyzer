import sqlite3
import _FrozenDir


class Database():
    def __init__(self):
        self._InitDB()
        pass

    def _InitDB(self):
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        dbPath = self.srcPath+r'\\database.db'
        self.conn = sqlite3.connect(dbPath, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._CitiesRowIT = 0
        self._AttractionsRowIT = 0
        self._Cname = []
        self._Curl = []
        self._Cname2 = []
        self._Aname = []
        self._AnameEn = []
        self._Percentage = []
        self._CityData = []
        self._AttractionData = []
        pass

    def _InitTB_Cities(self):
        try:
            self.cursor.execute('''drop table Cities''')
        except Exception as e:
            pass
        try:
            self.cursor.execute(
                '''CREATE TABLE "Cities" (
	                "Cname"	        TEXT NOT NULL,
	                "Curl"	        TEXT NOT NULL UNIQUE,
	                PRIMARY KEY("Curl")
                )
                ''')
            self.conn.commit()
        except Exception as e:
            pass
        pass

    def _InitTB_Attractions(self):
        try:
            self.cursor.execute('''drop table Attractions''')
        except Exception as e:
            pass
        try:
            self.cursor.execute(
                '''CREATE TABLE "Attractions" (
	                "Cname"	        TEXT NOT NULL,
	                "Aname"	        TEXT NOT NULL,
                    "AnameEn"       TEXT NOT NULL,
	                "Percentage"	REAL NOT NULL
                )
                ''')
            self.conn.commit()
        except Exception as e:
            pass
        pass

    def _SQL(self, sql, default):
        if(default == True):
            try:
                self.cursor.execute('''''')
                self.conn.commit()
                pass
            except Exception as e:
                pass
            pass
        else:
            try:
                result = self.cursor.execute(sql)
                self.conn.commit()
                return result
            except Exception as e:
                pass
            pass

    def _InitCitiesData(self, cname, curl):
        self._Cname.append(cname)
        self._Curl.append(curl)
        self._CityData.append((self._Cname[self._CitiesRowIT],
                              self._Curl[self._CitiesRowIT]))
        print(self._CityData[self._CitiesRowIT])
        sql = '''insert into Cities values''' + \
            str(self._CityData[self._CitiesRowIT])
        self.cursor.execute(sql)
        self._CitiesRowIT = self._CitiesRowIT+1
        self.conn.commit()
        pass

    def _InitAttractionsData(self, cname, aname, anameen, percentage):
        self._Cname2.append(cname)
        self._Aname.append(aname)
        self._AnameEn.append(anameen)
        self._Percentage.append(percentage)
        self._AttractionData.append((self._Cname2[self._AttractionsRowIT],
                                     self._Aname[self._AttractionsRowIT],
                                     self._AnameEn[self._AttractionsRowIT],
                                     self._Percentage[self._AttractionsRowIT]))
        print(self._AttractionData[self._AttractionsRowIT])
        sql = '''insert into Attractions values''' + \
            str(self._AttractionData[self._AttractionsRowIT])
        self.cursor.execute(sql)
        self._AttractionsRowIT = self._AttractionsRowIT+1
        self.conn.commit()
        pass
