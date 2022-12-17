# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesdhedsm.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLayout,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(861, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.pgTools = QWidget()
        self.pgTools.setObjectName(u"pgTools")
        self.pgTools.setStyleSheet(u"font-size: 14pt;")
        self.page_Connections_layout = QVBoxLayout(self.pgTools)
        self.page_Connections_layout.setSpacing(5)
        self.page_Connections_layout.setObjectName(u"page_Connections_layout")
        self.page_Connections_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.page_Connections_layout.setContentsMargins(10, 0, 5, 5)
        self.tblTools = QTableWidget(self.pgTools)
        self.tblTools.setObjectName(u"tblTools")

        self.page_Connections_layout.addWidget(self.tblTools)

        self.pages.addWidget(self.pgTools)
        self.page_Main = QWidget()
        self.page_Main.setObjectName(u"page_Main")
        self.page_main_layout = QVBoxLayout(self.page_Main)
        self.page_main_layout.setSpacing(5)
        self.page_main_layout.setObjectName(u"page_main_layout")
        self.page_main_layout.setContentsMargins(5, 5, 5, 5)
        self.pages.addWidget(self.page_Main)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.laytest = QHBoxLayout()
        self.laytest.setSpacing(0)
        self.laytest.setObjectName(u"laytest")
        self.laytest.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout.addLayout(self.laytest)

        self.tblConnections = QTableWidget(self.page_3)
        self.tblConnections.setObjectName(u"tblConnections")

        self.verticalLayout.addWidget(self.tblConnections)


        self.page_3_layout.addLayout(self.verticalLayout)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
    # retranslateUi

