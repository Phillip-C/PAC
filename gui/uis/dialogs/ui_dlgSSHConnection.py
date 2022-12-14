# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgSSHConnectionDTWVzS.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_dlgSSHConnection(QDialog):
    def setupUi(self, dlgSSHConnection):
        if not dlgSSHConnection.objectName():
            dlgSSHConnection.setObjectName(u"dlgSSHConnection")
        dlgSSHConnection.resize(213, 196)
        self.buttonBox = QDialogButtonBox(dlgSSHConnection)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 160, 191, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(dlgSSHConnection)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 16, 194, 141))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.txtNickname = QLineEdit(self.layoutWidget)
        self.txtNickname.setObjectName(u"txtNickname")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtNickname)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.txtSSHHost = QLineEdit(self.layoutWidget)
        self.txtSSHHost.setObjectName(u"txtSSHHost")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txtSSHHost)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.txtSSHUser = QLineEdit(self.layoutWidget)
        self.txtSSHUser.setObjectName(u"txtSSHUser")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txtSSHUser)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.txtSSHPassword = QLineEdit(self.layoutWidget)
        self.txtSSHPassword.setObjectName(u"txtSSHPassword")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.txtSSHPassword)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.btnSSHPrivateKey = QPushButton(self.layoutWidget)
        self.btnSSHPrivateKey.setObjectName(u"btnSSHPrivateKey")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.btnSSHPrivateKey)

        self.txtPrivateKey = QLabel(dlgSSHConnection)
        self.txtPrivateKey.setObjectName(u"txtPrivateKey")
        self.txtPrivateKey.setGeometry(QRect(10, 150, 49, 16))
        self.txtPrivateKey.setStyleSheet(u"visibility: hidden")
        self.txtPrivateKey.setTextFormat(Qt.PlainText)
        self.retranslateUi(dlgSSHConnection)
        self.buttonBox.accepted.connect(dlgSSHConnection.accept)
        self.buttonBox.rejected.connect(dlgSSHConnection.reject)

        QMetaObject.connectSlotsByName(dlgSSHConnection)
    # setupUi

    def retranslateUi(self, dlgSSHConnection):
        dlgSSHConnection.setWindowTitle(QCoreApplication.translate("dlgSSHConnection", u"Add Connection", None))
        self.label.setText(QCoreApplication.translate("dlgSSHConnection", u"Nickname", None))
        self.label_2.setText(QCoreApplication.translate("dlgSSHConnection", u"Host/IP", None))
        self.label_3.setText(QCoreApplication.translate("dlgSSHConnection", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("dlgSSHConnection", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("dlgSSHConnection", u"Private Key", None))
        self.btnSSHPrivateKey.setText(QCoreApplication.translate("dlgSSHConnection", u"Select Private Key", None))
        self.txtPrivateKey.setText("")
    # retranslateUi

