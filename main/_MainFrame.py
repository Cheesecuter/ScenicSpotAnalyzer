import _lang
import _FrozenDir
import _DBGrid
import _Database
import _Crawl
import _InfoFrame
import csv
import time
import re
import wx.grid
import wx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


class MainFrame(wx.Frame):
    def __init__(self, superior):
        self._lang_ = _lang._Language()
        # wx.Frame.__init__(self, parent=superior,
        #                   style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))
        wx.Frame.__init__(self, parent=superior,
                          style=wx.DEFAULT_FRAME_STYLE)
        self.SetTitle(self._lang_._mframe_FrameTitle)
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        iconPath = self.srcPath+r'\\icon.png'
        self.SetIcon(wx.Icon(iconPath))
        self.SetSize((900, 700))
        self.Center()
        self.SetOwnBackgroundColour("#b3b3b3")
        # panel
        self.panelMainFrame = wx.Panel(
            self, -1, pos=(0, 0), size=(900, 700))
        self.panelMainFrame.SetBackgroundColour("#eeeeee")

        self._initOperators()
        self._initGrid()

        self._DB = _Database.Database()
        self._menuBar()
        pass

    def _menuBar(self):
        self.menuBar = wx.MenuBar()

        self.fileMenu = wx.Menu()
        self.menuBar.Append(self.fileMenu, self._lang_._mframe_menu_file)
        self._inittablessM = self.fileMenu.Append(
            -1, self._lang_._mframe_menu_file_initTables)
        self.Bind(wx.EVT_MENU, self._initTables_f, self._inittablessM)
        self._initdatasM = self.fileMenu.Append(-1,
                                                self._lang_._mframe_menu_file_initDatas)
        self.Bind(wx.EVT_MENU, self._initDatas_f, self._initdatasM)
        self.fileMenu.AppendSeparator()
        self._exitM = self.fileMenu.Append(-1,
                                           self._lang_._mframe_menu_file_exit)
        self.Bind(wx.EVT_MENU, self._exit_f, self._exitM)

        self.viewMenu = wx.Menu()
        self.menuBar.Append(self.viewMenu, self._lang_._mframe_menu_view)
        self._citiesgrid_M = self.viewMenu.Append(
            -1, self._lang_._mframe_menu_view_citiesGrid)
        self.Bind(wx.EVT_MENU, self._citiesGrid_f, self._citiesgrid_M)

        self.toolsMenu = wx.Menu()
        self.menuBar.Append(self.toolsMenu, self._lang_._mframe_menu_tools)
        self._languageM = self.toolsMenu.Append(-1,
                                                self._lang_._mframe_menu_tools_language)
        self.Bind(wx.EVT_MENU, self._language_f, self._languageM)

        self.helpMenu = wx.Menu()
        self.menuBar.Append(self.helpMenu, self._lang_._mframe_menu_help)
        self._aboutM = self.helpMenu.Append(-1,
                                            self._lang_._mframe_menu_help_about)
        self.Bind(wx.EVT_MENU, self._about_f, self._aboutM)

        self.SetMenuBar(self.menuBar)

    def _initTables_f(self, event):
        print(self._lang_._mframe_emsg__initTables_f_is_running)
        self._DB._InitTB_Cities()
        self._DB._InitTB_Attractions()
        print(self._lang_._mframe_emsg_Database_initiated)
        print(self._lang_._mframe_emsg__initTables_f_is_done)
        pass

    def _initDatas_f(self, event):
        print(self._lang_._mframe_emsg__initDatas_f_is_running)
        crawl = _Crawl.Crawl(self._DB)
        crawl._save()
        print(self._lang_._mframe_emsg_Crawl_data_initiated)
        print(self._lang_._mframe_emsg__initDatas_f_is_done)
        pass

    def _exit_f(self, event):
        print(self._lang_._mframe_emsg__exit_f_is_running)
        self.Close(True)
        wx.Exit()

    def _citiesGrid_f(self, event):
        print(self._lang_._mframe_emsg__citiesGrid_f_is_running)
        self.cityGrid = _DBGrid.GridControl(None, self._lang_)
        self.cityGrid.Show()
        print(self._lang_._mframe_emsg__citiesGrid_f_is_done)
        pass

    def _language_f(self, event):
        print(self._lang_._mframe_emsg__language_f_is_running)
        path = self.srcPath+r'\\langType.txt'
        f = open(path,
                 mode="r", encoding="UTF-8")
        langType = f.readline()
        if(langType == 'en_US'):
            f = open(path,
                     mode="w", encoding="UTF-8")
            f.write('zh_CN')
            print(langType+" => zh_CN")
            print(self._lang_._mframe_emsg_Language_Changed_Successfully_1n)
            f.close()
        if(langType == 'zh_CN'):
            f = open(path,
                     mode="w", encoding="UTF-8")
            f.write('en_US')
            print(langType+" => en_US")
            print(self._lang_._mframe_emsg_Language_Changed_Successfully_1n)
            f.close()
        print(self._lang_._mframe_emsg__language_f_is_done)
        pass

    def _about_f(self, event):
        print(self._lang_._mframe_emsg__about_f_is_running)
        infoFrame = _InfoFrame.InfoFrame(None, self._lang_)
        infoFrame.Show(True)
        print(self._lang_._mframe_emsg__about_f_is_done)
        pass

    def _initOperators(self):
        self.txtInputCname = wx.StaticText(parent=self.panelMainFrame, id=-1, label=self._lang_._mframe_panel_txtInputCname,
                                           pos=(10, 10), size=(100, 20), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.inputCname = wx.TextCtrl(
            parent=self.panelMainFrame, pos=(10, 30), size=(100, 25))
        self.btSelectBname = wx.Button(parent=self.panelMainFrame, pos=(120, 30), size=(100, 25),
                                       label=self._lang_._mframe_panel_btCheck)
        self.Bind(wx.EVT_BUTTON, self._btInitAttractionsGrid_f,
                  self.btSelectBname)
        self.btInsertBname = wx.Button(parent=self.panelMainFrame, pos=(230, 30), size=(100, 25),
                                       label=self._lang_._mframe_panel_btShowPlot)
        self.Bind(wx.EVT_BUTTON, self._btGetPlot_f, self.btInsertBname)
        pass

    def _btInitAttractionsGrid_f(self, event):
        cname = str(self.inputCname.GetValue())
        sql = '''
        select * from Attractions
        where Cname="'''+cname+'"'
        print(sql)
        result = self._DB._SQL(sql, False)
        self._emptyGrid()
        rowNo = 0
        for row in result:
            colNo = 0
            for it in row:
                self.grid.SetCellValue(rowNo, colNo, str(it))
                colNo += 1
            rowNo += 1
        pass

    def _emptyGrid(self):
        for row in range(0, 10):
            for col in range(0, 3):
                self.grid.SetCellValue(row, col, '')
        pass

    def _btGetPlot_f(self, event):
        cname = str(self.inputCname.GetValue())
        sql = '''
        select * from Attractions
        where Cname="'''+cname+'"'
        result = self._DB._SQL(sql, False)
        x = []
        y = []
        for i in result:
            x.append(str(i[2]))
            y.append(i[3])
        sql = '''
        select Curl from Cities
        where Cname="'''+cname+'"'
        titleResult = self._DB._SQL(sql, False)
        print(type(titleResult))
        for i in titleResult:
            title = re.sub(
                r".*?-.*?-(?P<title>.*?)", '', str(i[0])
            )
            print(title)
        plt.figure(title, figsize=(12, 6))
        plt.title(title)
        barh = plt.barh(x, y, color="#eeeeee", edgecolor="black")
        plt.bar_label(barh, fmt='%g%%')
        plt.show()
        pass

    def _initGrid(self):
        self.grid = wx.grid.Grid(self.panelMainFrame, -1, pos=(0, 90),
                                 size=(500, 260), style=wx.WANTS_CHARS, name=self._lang_._mframe_grid_Name)
        self.grid.CreateGrid(10, 4, selmode=wx.grid.Grid.SelectCells)
        self.grid.EnableEditing(True)
        self.grid.SetColLabelValue(0, self._lang_._mframe_grid_CityName)
        self.grid.SetColSize(0, 100)
        self.grid.SetColLabelValue(
            1, self._lang_._mframe_grid_AttractionNameCN)
        self.grid.SetColSize(1, 100)
        self.grid.SetColLabelValue(
            2, self._lang_._mframe_grid_AttractionNameUS)
        self.grid.SetColSize(2, 100)
        self.grid.SetColLabelValue(3, self._lang_._mframe_grid_Percentage)
        self.grid.SetColSize(3, 100)
        for i in range(0, 10):
            self.grid.SetRowSize(i, 30)
        pass

    # This method is a placeholder.
    # 此方法为占位符.
    def _empty(self, event):
        pass
