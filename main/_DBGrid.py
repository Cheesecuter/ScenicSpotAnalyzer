import wx
import wx.grid
import csv
import _FrozenDir
import _Database
import _lang


class GridControl(wx.Frame):

    def __init__(self, superior, lang):

        self._lang_ = lang
        #self._lang_ = _lang._Language()
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        wx.Frame.__init__(self, parent=superior,
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))
        self.SetTitle(self._lang_._dbgrid_FrameTitle)
        iconPath = self.srcPath+r'\\icon.png'
        self.SetIcon(wx.Icon(iconPath))
        self.SetSize((560, 600))
        self.Center()
        self.panelGrid = wx.Panel(
            self, -1, pos=(0, 0), size=(560, 600))
        self.panelGrid.SetBackgroundColour("#eeeeee")

        self.grid = wx.grid.Grid(self.panelGrid, -1, pos=(0, 0),
                                 size=(540, 560), style=wx.WANTS_CHARS, name=self._lang_._dbgrid_GridTitle)
        self.grid.CreateGrid(400, 2, selmode=wx.grid.Grid.SelectCells)
        self.grid.EnableEditing(False)

        self.grid.SetColLabelValue(0, self._lang_._dbgrid_gridCOL_City_Name)
        self.grid.SetColSize(0, 100)
        self.grid.SetColLabelValue(1, self._lang_._dbgrid_gridCOL_City_URL)
        self.grid.SetColSize(1, 300)

        csvPath = self.srcPath+r'\\Cities.csv'
        with open(csvPath, encoding='UTF-8-SIG') as f:
            rowNo = 0
            for row in csv.reader(f, skipinitialspace=True):
                if(row == []):
                    continue
                if(row[0] == 'Cname'):
                    continue
                self.grid.SetCellValue(rowNo, 0, row[0])
                self.grid.SetCellValue(rowNo, 1, row[1])
                rowNo += 1
                pass
        self._DB = _Database.Database()
