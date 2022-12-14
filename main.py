from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
from qt_core import *
from gui.core.json_settings import Settings
from gui.uis.windows.main_window import *
from gui.widgets import *
from gui.uis.dialogs import ui_dlgSSHConnection
import ntpath # support filepaths on all os
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.loc_settings = settings
        self.settings_vals = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.populate_cboConnections()
        self.show()

    def populate_cboConnections(self):
        self.ui.cboConnections.addItem("") # one empty item
        for item in self.settings_vals["ssh_connections"]:
            self.ui.cboConnections.addItem(item["name"])

    def btnSelectPrivateKey_Click(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Private Key')
        self.txtPrivateKey.setText(filename)
        
    def btnDeleteSSH_Click(self):       
        button = QMessageBox.question(self, "Are you sure you?", "Are you sure you want to delete this connection?")
        if button == QMessageBox.No:
            return
        if len(self.ui.load_pages.tblConnections.selectedItems()) > 0:
            for item in self.ui.load_pages.tblConnections.selectedItems():
                if item != None:
                    del self.settings_vals["ssh_connections"][item.row()]
                    self.ui.load_pages.tblConnections.removeRow(item.row())
                    self.loc_settings.serialize()

    def btnAddConnection_Click(self):
        dlg = ui_dlgSSHConnection.Ui_dlgSSHConnection()
        dlg.setupUi(dlg)
        dlg.btnSSHPrivateKey.clicked.connect(self.btnSelectPrivateKey_Click)
        dlg.exec()
        nick = dlg.txtNickname.text()
        host = dlg.txtSSHHost.text()
        user = dlg.txtSSHUser.text()
        pwd = dlg.txtSSHPassword.text()
        key = dlg.PrivateKey
        if nick == "" or host == "" or user == "": return
        self.settings_vals["ssh_connections"].append({"name":nick, "host":host, "username":user, "password":pwd})
        self.loc_settings.serialize()
        while self.ui.load_pages.tblConnections.rowCount() > 0:
            self.ui.load_pages.tblConnections.removeRow(0)
        for con in self.settings_vals["ssh_connections"]:
            row_number = self.ui.load_pages.tblConnections.rowCount()
            self.ui.load_pages.tblConnections.insertRow(row_number) # Insert row
            self.ui.load_pages.tblConnections.setItem(row_number, 0, QTableWidgetItem(str(con["name"]))) 
            self.ui.load_pages.tblConnections.setItem(row_number, 1, QTableWidgetItem(str(con["host"]))) 
            self.ui.load_pages.tblConnections.setItem(row_number, 2, QTableWidgetItem(str(con["username"]))) 
            key = None
            if len(str(con["key"])) > 0:
                key = ntpath.basename(str(con["key"])) # private key file name
            self.ui.load_pages.tblConnections.setItem(row_number, 3, QTableWidgetItem(str("key"))) 
            self.ui.load_pages.tblConnections.setRowHeight(row_number, 22)
        del dlg

    def tblConnections_SelectionChanged(self):
        if len(self.ui.load_pages.tblConnections.selectedItems()) > 0:
            self.ui.tbplug.setEnabled(True)
            self.ui.tbdel.setEnabled(True)
        elif len(self.ui.load_pages.tblConnections.selectedItems()) == 0:
            self.ui.tbplug.setEnabled(False)
            self.ui.tbdel.setEnabled(False)

    def itemClick_evt(self,item):
        if item.text() == "Connections":
            MainFunctions.set_page(self,self.ui.load_pages.page_Connections)
        return item.text()

    def SSHitemClick_evt(self,item):
        if item.text() == 1:
            self.ui.load_pages.txtSSHNickName.setPlainText(str(self.ui.load_pages.tblConnections.item(item.row(),0).text()))
            self.ui.load_pages.txtSSHHostIP.setPlainText(str(self.ui.load_pages.tblConnections.item(item.row(),1).text()))
            self.ui.load_pages.txtSSHUsername.setPlainText(str(self.ui.load_pages.tblConnections.item(item.row(),2).text()))
        elif self == 2:
            self.actHi = QAction(self)
            self.actHi.setText("Hello")
            self.mnu = QMenu(self)
            self.mnu.addAction(self.actHi)

    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)
        top_btn_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        
        if btn.objectName() == "btn_home":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self,self.ui.load_pages.page_Connections)
        if btn.objectName() == "btn_targets":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self,self.ui.load_pages.page_Main)
        if btn.objectName() == "btn_adversary":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self,self.ui.load_pages.page_3)
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            top_btn_settings.set_active(False)

            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column": # this is default name
                    self.ui.left_menu.deselect_all_tab()
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu = self.ui.left_column.menus.menu_1,
                    title = "Settings",
                    icon_path = Functions.set_svg_icon("icon_settings")
                )

        if btn.objectName() == "btn_info" or btn.objectName() == "btn_close_left_column":
            top_btn_settings.set_active(False)

            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column": # this is default name
                    self.ui.left_menu.deselect_all_tab()
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu = self.ui.left_column.menus.menu_2,
                    title = "Info & Help",
                    icon_path = Functions.set_svg_icon("icon_info")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Settings            
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)   

            # Get Left Menu Info            
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_info")
            top_settings.set_active_tab(False)         

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
    


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())

