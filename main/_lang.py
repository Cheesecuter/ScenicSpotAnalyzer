import os
import _FrozenDir


class _Language:
    def __init__(self):
        path = _FrozenDir.app_path()+r'\\src\\langType.txt'
        print(path)
        f = open(path,
                 mode="r", encoding="UTF-8")
        langType = f.readline()
        if(langType == 'en_US'):
            print("lang: "+langType)
            self._en_US()
            f.close()
        if(langType == 'zh_CN'):
            print("语言: "+langType)
            self._zh_CN()
            f.close()
        pass

    def _en_US(self):
        # ********************
        # Main Frame
        # ********************
        # frames
        self._mframe_FrameTitle = "ScenicSpotAnalyzer"
        # menus
        self._mframe_menu_file = "File"
        self._mframe_menu_file_initTables = "Init Tables"
        self._mframe_menu_file_initDatas = "Init Datas"
        self._mframe_menu_file_exit = "Exit"
        self._mframe_menu_view = "View"
        self._mframe_menu_view_citiesGrid = "Cities Grid"
        self._mframe_menu_tools = "Tools"
        self._mframe_menu_tools_language = "Language"
        self._mframe_menu_help = "Help"
        self._mframe_menu_help_about = "About"
        # end message
        self._mframe_emsg__initTables_f_is_running = "_initTables_f is running"
        self._mframe_emsg_Database_initiated = "Database initiated"
        self._mframe_emsg__initTables_f_is_done = "_initTables_f is done"
        self._mframe_emsg__initDatas_f_is_running = "_initDatas_f is running"
        self._mframe_emsg_Craw_data_initiated = "Craw data initiated"
        self._mframe_emsg__initDatas_f_is_done = "_initDatas_f is done"
        self._mframe_emsg__exit_f_is_running = "_exit_f is running"
        self._mframe_emsg__citiesGrid_f_is_running = "_citiesGrid_f is running"
        self._mframe_emsg__citiesGrid_f_is_done = "_citiesGrid_f is done"
        self._mframe_emsg__language_f_is_running = "_language_f is running"
        self._mframe_emsg_Language_Changed_Successfully_1n = "Language Changed Successfully\n"
        self._mframe_emsg__language_f_is_done = "_language_f is done"
        self._mframe_emsg__about_f_is_running = "_about_f is running"
        self._mframe_emsg__about_f_is_done = "_about_f is done"
        # panels
        self._mframe_panel_txtInputCname = "City Name"
        self._mframe_panel_btCheck = "Check"
        self._mframe_panel_btShowPlot = "Show Plot"
        # grid
        self._mframe_grid_Name = "Attractions"
        self._mframe_grid_CityName = "Number"
        self._mframe_grid_AttractionNameCN = "Spot Name"
        self._mframe_grid_AttractionNameUS = "Spot Name"
        self._mframe_grid_Percentage = "Percentage"

        # ********************
        # DB Grid
        # ********************
        # frames
        self._dbgrid_FrameTitle = "Cities"
        # grid
        self._dbgrid_GridTitle = "Cities"
        self._dbgrid_gridCOL_City_Name = "City Name"
        self._dbgrid_gridCOL_City_URL = "City URL"

        # ********************
        # Info Frame
        # ********************
        # frames
        self._abframe_FrameTitle = "About"
        # informations
        self._abframe_info_1 = "Scenic Spot Analyzer"
        self._abframe_info_2 = "v0.0.2"
        self._abframe_info_3 = "2004010525"
        self._abframe_info_4 = "HRBUST"
        pass

    def _zh_CN(self):
        # ********************
        # 主窗口
        # ********************
        # 窗口
        self._mframe_FrameTitle = "景区分析器"
        # 菜单
        self._mframe_menu_file = "文件"
        self._mframe_menu_file_initTables = "初始化表"
        self._mframe_menu_file_initDatas = "初始化数据"
        self._mframe_menu_file_exit = "退出"
        self._mframe_menu_view = "视图"
        self._mframe_menu_view_citiesGrid = "城市列表"
        self._mframe_menu_tools = "工具"
        self._mframe_menu_tools_language = "语言"
        self._mframe_menu_help = "帮助"
        self._mframe_menu_help_about = "关于"
        # 终端信息
        self._mframe_emsg__initTables_f_is_running = "调用 _initTables_f"
        self._mframe_emsg_Database_initiated = "数据库初始化成功"
        self._mframe_emsg__initTables_f_is_done = "_initTables_f 调用完成"
        self._mframe_emsg__initDatas_f_is_running = "调用 _initDatas_f"
        self._mframe_emsg_Craw_data_initiated = "数据爬取完成"
        self._mframe_emsg__initDatas_f_is_done = "_initDatas_f 调用完成"
        self._mframe_emsg__exit_f_is_running = "调用 _exit_f"
        self._mframe_emsg__citiesGrid_f_is_running = "调用 _citiesGrid_f"
        self._mframe_emsg__citiesGrid_f_is_done = "_citiesGrid_f 调用完成"
        self._mframe_emsg__language_f_is_running = "调用 _language_f"
        self._mframe_emsg_Language_Changed_Successfully_1n = "语言切换成功\n"
        self._mframe_emsg__language_f_is_done = "_language_f 调用完成"
        self._mframe_emsg__about_f_is_running = "调用 _about_f"
        self._mframe_emsg__about_f_is_done = "_about_f 调用完成"
        # 面板
        self._mframe_panel_txtInputCname = "城市名称"
        self._mframe_panel_btCheck = "查看"
        self._mframe_panel_btShowPlot = "显示柱状图"
        # 表格
        self._mframe_grid_Name = "风景区"
        self._mframe_grid_CityName = "城市名称"
        self._mframe_grid_AttractionNameCN = "景区名称"
        self._mframe_grid_AttractionNameUS = "景区名称"
        self._mframe_grid_Percentage = "游客百分比"

        # ********************
        # 数据表格
        # ********************
        # 窗口
        self._dbgrid_FrameTitle = "城市"
        # 表格
        self._dbgrid_GridTitle = "城市"
        self._dbgrid_gridCOL_City_Name = "城市名称"
        self._dbgrid_gridCOL_City_URL = "城市URL"

        # ********************
        # 信息窗口
        # ********************
        # 窗口
        self._abframe_FrameTitle = "关于"
        # 信息
        self._abframe_info_1 = "景区分析器"
        self._abframe_info_2 = "v0.0.2"
        self._abframe_info_3 = "2004010525"
        self._abframe_info_4 = "HRBUST"
        pass
