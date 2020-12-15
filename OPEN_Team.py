# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OPEN_Team.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
cricket=sqlite3.connect('Fantacycricket.db')
curcricket=cricket.cursor()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(688, 591)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.selectname = QtWidgets.QLineEdit(self.frame)
        self.selectname.setObjectName("selectname")
        self.horizontalLayout.addWidget(self.selectname)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.teamlist = QtWidgets.QListWidget(self.frame)
        self.teamlist.setObjectName("teamlist")
        self.verticalLayout_2.addWidget(self.teamlist)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.frame)
        self.openteamlist()
        self.teamlist.itemClicked.connect(self.lineselect)
               
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.open_team)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Open Team"))
        self.label.setText(_translate("Dialog", "Choose the Team from the list:"))

    def openteamlist(self):
        self.query="SELECT * FROM team"
        curcricket.execute(self.query)
        self.fopen=curcricket.fetchall()
        for player in self.fopen:
            self.teamlist.addItem(str(player[1]))
            
    def lineselect(self,item):
        self.selectname.setText(item.text())

    def __init__(self):
        self.flag_ = False
        
    def open_team(self): 
        self.team_name  = self.selectname.text()
        if self.team_name:
            self.query = "SELECT * FROM team WHERE Team_name='{}'".format(self.team_name)
            curcricket.execute(self.query)
            self.data = curcricket.fetchone()
            if self.data != None:
                self.flag_ = True
            else:
                msg=QMessageBox()
                msg.setWindowTitle("Open")
                msg.setText("Team not found.\t\t")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
