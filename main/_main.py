import wx
import _GUI


class MainClass:
    def __init__(self):
        self.app = wx.App()
        self._gui = _GUI.GUIClass()
        self.app.MainLoop()
        pass
