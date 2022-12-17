from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os
from qt_core import *
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from gui.widgets import *
from . ui_main import *
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    tbl = None
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "Antivirus.svg",
            "btn_id" : "btn_targets",
            "btn_text" : "Targets",
            "btn_tooltip" : "Endpoints to be targeted for attack.",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_emoticons.svg",
            "btn_id" : "btn_adversary",
            "btn_text" : "Advesary Tools",
            "btn_tooltip" : "Execute attacks on targets",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_info",
            "btn_text" : "Information",
            "btn_tooltip" : "Help and Information",
            "show_top" : False,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_settings",
            "btn_text" : "Settings",
            "btn_tooltip" : "Open settings page",
            "show_top" : False,
            "is_active" : False
        }
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings_vals["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings_vals["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings_vals["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)
        #self.ui.load_pages.btnDeleteSSH.clicked.connect(self.btnDeleteSSH_Click)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings_vals["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings_vals["app_name"])
        else:
            self.ui.title_bar.set_title("Operators Control Panel")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_Main)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # ADD CUSTOM WIDGETS
        self.btn_1 = PyPushButton(
            text = "Btn 1",
            radius = 8,
            color = self.themes["app_color"]["text_active"],
            bg_color= self.themes["app_color"]["dark_four"],
            bg_color_hover=self.themes["app_color"]["context_hover"],
            bg_color_pressed = self.themes["app_color"]["context_pressed"],
        )
        self.btn_1.setIcon(QIcon(Functions.set_svg_icon("card-circus-fair-svgrepo-com.svg")))
        self.btn_1.setMinimumHeight(40)
        self.ui.right_column.btn_1_layout.addWidget(self.btn_1)


        style_btn = '''
            QPushButton {{
                border: none;
                padding-left: 10px;
                padding-right: 5px;
                color: {_color};
                border-radius: {_radius};	
                background-color: {_bg_color};
            }}
            QPushButton:hover {{
                background-color: {_bg_color_hover};
            }}
            QPushButton:pressed {{	
                background-color: {_bg_color_pressed};
            }}
        '''
        button_style = style_btn.format(
            _color = self.themes["app_color"]["text_active"],
            _radius = 8,
            _bg_color = self.themes["app_color"]["dark_four"],
            _bg_color_hover = self.themes["app_color"]["context_hover"],
            _bg_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        ###
        ### Style for buttons, example below
        ###
        #self.ui.load_pages.btnAddConnection.setStyleSheet(button_style)
        
        txtStyle = f"""
            background-color: {self.themes["app_color"]["dark_one"]};
            border_size: 0px solid transparent;
            border-radius: 0px;
            padding-left: 10px;
            padding-right: 10px;
        """
        
        ###
        ### Style for txt
        ###
        #self.ui.load_pages.txtSSHUsername.setStyleSheet(txtStyle)
        #self.ui.load_pages.txtSSHPassword.setStyleSheet(txtStyle)
        #self.ui.load_pages.btnAddConnection.setIcon(QIcon(Functions.set_svg_icon("icon_computer")))
        #self.ui.load_pages.btnDeleteSSH.setIcon(QIcon(Functions.set_svg_icon("icon_skull")))

        ### SETTINGS MENU
        self.mnuSettingsWidget = QListWidget()
        self.mnuSettingsWidget.setStyleSheet(f"""
            background-color: {self.themes["app_color"]["bg_two"]};
            font: 20pt {self.settings["font"]["family"]};
        """)
        self.mnuSettingsWidget.setFrameStyle(0)
        #for x in self.settings["ssh_connections"]:
        ### Connections
        item = QListWidgetItem(f"""Connections""")
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item.setSizeHint(QSize(0, 70))
        self.mnuSettingsWidget.addItem(item)
        self.mnuSettingsWidget.itemClicked.connect(self.itemClick_evt)
        self.ui.left_column.menus.mnuSettings.addWidget(self.mnuSettingsWidget)
        style = '''
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QTableWidget */

QTableWidget {{	
	background-color: {_bg_color};
	padding: 5px;
	border-radius: {_radius}px;
	gridline-color: {_grid_line_color};
    color: {_color};
}}
QTableWidget::item{{
	border-color: none;
	padding-left: 5px;
	padding-right: 5px;
	gridline-color: rgb(44, 49, 60);
    border-bottom: 1px solid {_bottom_line_color};
}}
QTableWidget::item:selected{{
	background-color: {_selection_color};
}}
QHeaderView::section{{
	background-color: rgb(33, 37, 43);
	max-width: 30px;
	border: 1px solid rgb(44, 49, 58);
	border-style: none;
    border-bottom: 1px solid rgb(44, 49, 60);
    border-right: 1px solid rgb(44, 49, 60);
}}
QTableWidget::horizontalHeader {{	
	background-color: rgb(33, 37, 43);
}}
QTableWidget QTableCornerButton::section {{
    border: none;
	background-color: {_header_horizontal_color};
	padding: 3px;
    border-top-left-radius: {_radius}px;
}}
QHeaderView::section:horizontal
{{
    border: none;
	background-color: {_header_horizontal_color};
	padding: 3px;
}}
QHeaderView::section:vertical
{{
    border: none;
	background-color: {_header_vertical_color};
	padding-left: 5px;
    padding-right: 5px;
    border-bottom: 1px solid {_bottom_line_color};
    margin-bottom: 1px;
}}


/* /////////////////////////////////////////////////////////////////////////////////////////////////
ScrollBars */
QScrollBar:horizontal {{
    border: none;
    background: {_scroll_bar_bg_color};
    height: 8px;
    margin: 0px 21px 0 21px;
	border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background: {_context_color};
    min-width: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    border: none;
    background: {_scroll_bar_btn_color};
    width: 20px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
    border: none;
    background: {_scroll_bar_btn_color};
    width: 20px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{{
     background: none;
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{{
     background: none;
}}
QScrollBar:vertical {{
	border: none;
    background: {_scroll_bar_bg_color};
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
}}
QScrollBar::handle:vertical {{	
	background: {_context_color};
    min-height: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:vertical {{
     border: none;
    background: {_scroll_bar_btn_color};
     height: 20px;
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
	border: none;
    background: {_scroll_bar_btn_color};
     height: 20px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     subcontrol-position: top;
     subcontrol-origin: margin;
}}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
     background: none;
}}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
     background: none;
}}
'''
        style_format = style.format(
            _radius = 8,          
            _color = self.themes["app_color"]["text_foreground"],
            _bg_color = self.themes["app_color"]["dark_two"],
            _header_horizontal_color = self.themes["app_color"]["dark_two"],
            _header_vertical_color = self.themes["app_color"]["bg_three"],
            _selection_color = self.themes["app_color"]["context_color"],
            _bottom_line_color = self.themes["app_color"]["bg_three"],
            _grid_line_color = self.themes["app_color"]["bg_one"],
            _scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            _scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            _context_color = self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.tblConnections.setStyleSheet(style_format)
        self.ui.load_pages.tblConnections.setColumnCount(4)
        self.ui.load_pages.tblConnections.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.load_pages.tblConnections.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.load_pages.tblConnections.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("NAME")
        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("HOST/IP")
        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("USERNAME")
        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText("Private Key")
        # Set column
        self.ui.load_pages.tblConnections.setHorizontalHeaderItem(0, self.column_1)
        self.ui.load_pages.tblConnections.setHorizontalHeaderItem(1, self.column_2)
        self.ui.load_pages.tblConnections.setHorizontalHeaderItem(2, self.column_3)
        self.ui.load_pages.tblConnections.setHorizontalHeaderItem(3, self.column_4)
        for con in self.settings["ssh_connections"]:
            row_number = self.ui.load_pages.tblConnections.rowCount()
            self.ui.load_pages.tblConnections.insertRow(row_number) # Insert row
            self.ui.load_pages.tblConnections.setItem(row_number, 0, QTableWidgetItem(str(con["name"]))) # Add name
            self.ui.load_pages.tblConnections.setItem(row_number, 1, QTableWidgetItem(str(con["host"]))) # Add nick
            self.ui.load_pages.tblConnections.setItem(row_number, 2, QTableWidgetItem(str(con["username"]))) # Add pass
            self.ui.load_pages.tblConnections.setItem(row_number, 3, QTableWidgetItem(str(con["key"]))) # Add key
            self.ui.load_pages.tblConnections.setRowHeight(row_number, 22)
        #self.ui.load_pages.tblConnections.itemClicked.connect(self.SSHitemClick_evt)
        self.ui.load_pages.tblConnections.itemSelectionChanged.connect(self.tblConnections_SelectionChanged)
        self.ui.load_pages.tblConnections.itemChanged.connect(self.tblConnections_itemChanged)

        ###
        ### Tools table
        ###
        self.ui.load_pages.tblTools.setStyleSheet(style_format)
        self.ui.load_pages.tblTools.setColumnCount(4)
        self.ui.load_pages.tblTools.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.load_pages.tblTools.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.load_pages.tblTools.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.clumn_1 = QTableWidgetItem()
        self.clumn_1.setTextAlignment(Qt.AlignCenter)
        self.clumn_1.setText("Type")
        self.clumn_2 = QTableWidgetItem()
        self.clumn_2.setTextAlignment(Qt.AlignCenter)
        self.clumn_2.setText("Tool")
        self.clumn_3 = QTableWidgetItem()
        self.clumn_3.setTextAlignment(Qt.AlignCenter)
        self.clumn_3.setText("Details")
        self.clumn_4 = QTableWidgetItem()
        self.clumn_4.setTextAlignment(Qt.AlignCenter)
        self.clumn_4.setText("Status")
        self.ui.load_pages.tblTools.setHorizontalHeaderItem(0, self.clumn_1)
        self.ui.load_pages.tblTools.setHorizontalHeaderItem(1, self.clumn_2)
        self.ui.load_pages.tblTools.setHorizontalHeaderItem(2, self.clumn_3)
        self.ui.load_pages.tblTools.setHorizontalHeaderItem(3, self.clumn_4)
        for con in self.settings["ssh_connections"]:
            row_number = self.ui.load_pages.tblTools.rowCount()
            self.ui.load_pages.tblTools.insertRow(row_number) # Insert row
            self.ui.load_pages.tblTools.setItem(row_number, 0, QTableWidgetItem(str(con["name"]))) # Add name
            self.ui.load_pages.tblTools.setItem(row_number, 1, QTableWidgetItem(str(con["host"]))) # Add nick
            self.ui.load_pages.tblTools.setItem(row_number, 2, QTableWidgetItem(str(con["username"]))) # Add pass
            self.ui.load_pages.tblTools.setItem(row_number, 3, QTableWidgetItem(str(con["key"]))) # Add key
            self.ui.load_pages.tblTools.setRowHeight(row_number, 22)

        style = '''
        QLineEdit {{
            background-color: {_bg_color};
            border-radius: {_radius}px;
            border: {_border_size}px solid transparent;
            padding-left: 10px;
            padding-right: 10px;
            selection-color: {_selection_color};
            selection-background-color: {_context_color};
            color: {_color};
        }}
        QLineEdit:focus {{
            border: {_border_size}px solid {_context_color};
            background-color: {_bg_color_active};
        }}
        '''
        style_format = style.format(
            _radius = 8,
            _border_size = 1,           
            _color = self.themes["app_color"]["text_foreground"],
            _selection_color = self.themes["app_color"]["context_color"],
            _bg_color = self.themes["app_color"]["dark_two"],
            _bg_color_active = self.themes["app_color"]["dark_three"],
            _context_color = self.themes["app_color"]["context_color"]
        )

        self.ui.tbadd.clicked.connect(self.btnAddConnection_Click)
        self.ui.tbdel.clicked.connect(self.btnDeleteSSH_Click)
        
    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)