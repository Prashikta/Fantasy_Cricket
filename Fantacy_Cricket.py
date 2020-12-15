# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fantacy_Cricket.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
cricket=sqlite3.connect('Fantacycricket.db')
curcricket=cricket.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 743)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(50, 40, 50, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_13.addWidget(self.label_2)
        self.bat = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.bat.setFont(font)
        self.bat.setStyleSheet("color: rgb(0, 170, 255);")
        self.bat.setObjectName("bat")
        self.horizontalLayout_13.addWidget(self.bat)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_13.addWidget(self.label_3)
        self.bow = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.bow.setFont(font)
        self.bow.setStyleSheet("color: rgb(0, 170, 255);")
        self.bow.setObjectName("bow")
        self.horizontalLayout_13.addWidget(self.bow)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_13.addWidget(self.label_4)
        self.ar = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.ar.setFont(font)
        self.ar.setStyleSheet("color: rgb(0, 170, 255);")
        self.ar.setObjectName("ar")
        self.horizontalLayout_13.addWidget(self.ar)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_13.addWidget(self.label_5)
        self.wk = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.wk.setFont(font)
        self.wk.setStyleSheet("color: rgb(0, 170, 255);")
        self.wk.setObjectName("wk")
        self.horizontalLayout_13.addWidget(self.wk)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.pointavail = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.pointavail.setFont(font)
        self.pointavail.setStyleSheet("color: rgb(0, 170, 255);")
        self.pointavail.setObjectName("pointavail")
        self.horizontalLayout_4.addWidget(self.pointavail)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("border:1px solid")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bat_rb = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.bat_rb.setFont(font)
        self.bat_rb.setStyleSheet("border:none")
        self.bat_rb.setObjectName("bat_rb")
        self.horizontalLayout_5.addWidget(self.bat_rb)
        self.bow_rb = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.bow_rb.setFont(font)
        self.bow_rb.setStyleSheet("border:none")
        self.bow_rb.setObjectName("bow_rb")
        self.horizontalLayout_5.addWidget(self.bow_rb)
        self.ar_rb = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.ar_rb.setFont(font)
        self.ar_rb.setStyleSheet("border:none")
        self.ar_rb.setObjectName("ar_rb")
        self.horizontalLayout_5.addWidget(self.ar_rb)
        self.wk_rb = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.wk_rb.setFont(font)
        self.wk_rb.setStyleSheet("border:none")
        self.wk_rb.setObjectName("wk_rb")
        self.horizontalLayout_5.addWidget(self.wk_rb)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.playerlist = QtWidgets.QListWidget(self.frame_3)
        self.playerlist.setStyleSheet("border:none")
        self.playerlist.setObjectName("playerlist")
        self.verticalLayout_4.addWidget(self.playerlist)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.pointused = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.pointused.setFont(font)
        self.pointused.setStyleSheet("color: rgb(0, 170, 255);")
        self.pointused.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pointused.setObjectName("pointused")
        self.horizontalLayout_6.addWidget(self.pointused)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("border:1px solid")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border:none")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.tname = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.tname.setFont(font)
        self.tname.setStyleSheet("color: rgb(0, 170, 255);  border:none")
        self.tname.setObjectName("tname")
        self.horizontalLayout_7.addWidget(self.tname)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.selectlist = QtWidgets.QListWidget(self.frame_4)
        self.selectlist.setStyleSheet("border:none")
        self.selectlist.setObjectName("selectlist")
        self.verticalLayout_6.addWidget(self.selectlist)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 26))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.menubar.setObjectName("menubar")
        self.menuManage_Team = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menuManage_Team.setFont(font)
        self.menuManage_Team.setObjectName("menuManage_Team")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.actionNEW_Team.setFont(font)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Team.addAction(self.actionNEW_Team)
        self.menuManage_Team.addAction(self.actionOPEN_Team)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionSAVE_Team)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Team.menuAction())
        self.actionNEW_Team.triggered.connect(self.newteam)
        self.actionOPEN_Team.triggered.connect(self.openteam)
        self.actionSAVE_Team.triggered.connect(self.saveteam)
        self.actionEVALUATE_Team.triggered.connect(self.evaluateteam)
        self.bat_rb.toggled.connect(self.checkstate)
        self.bow_rb.toggled.connect(self.checkstate)
        self.ar_rb.toggled.connect(self.checkstate)
        self.wk_rb.toggled.connect(self.checkstate)
        self.playerlist.doubleClicked.connect(self.changelist1)
        self.selectlist.doubleClicked.connect(self.changelist2)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_2.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.bat.setText(_translate("MainWindow", "##"))
        self.label_3.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.bow.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Allrounder (AR)"))
        self.ar.setText(_translate("MainWindow", "##"))
        self.label_5.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.wk.setText(_translate("MainWindow", "##"))
        self.label_7.setText(_translate("MainWindow", "Points Available"))
        self.pointavail.setText(_translate("MainWindow", "  ####"))
        self.bat_rb.setText(_translate("MainWindow", "BAT"))
        self.bow_rb.setText(_translate("MainWindow", "BOW"))
        self.ar_rb.setText(_translate("MainWindow", "AR"))
        self.wk_rb.setText(_translate("MainWindow", "WK"))
        self.label_6.setText(_translate("MainWindow", ">"))
        self.label_13.setText(_translate("MainWindow", "Points Used"))
        self.pointused.setText(_translate("MainWindow", "  ####"))
        self.label_15.setText(_translate("MainWindow", "Team Name"))
        self.tname.setText(_translate("MainWindow", "Displayed Here"))
        self.menuManage_Team.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionOPEN_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def newteam(self):
        from NEW_Team import Ui_Dialog
        dialog = QtWidgets.QDialog()
        nw = Ui_Dialog()
        nw.setupUi(dialog)
        dialog.exec_()
        if nw.flag_:
            self.selectlist.clear()
            self.fetchteam(nw.team_name)
            self.bat_rb.setChecked(True)
            self.checkstate()

    def evaluateteam(self):
        from EVALUATE_Team import Ui_Form
        dialog = QtWidgets.QDialog()
        ev = Ui_Form()
        ev.setupUi(dialog)
        dialog.exec_()

    def openteam(self):
        from OPEN_Team import Ui_Dialog
        dialog = QtWidgets.QDialog()
        op = Ui_Dialog()
        op.setupUi(dialog)
        dialog.exec_()
        if op.flag_:
            self.selectlist.clear()
            self.fetchteam(op.team_name)
            self.bat_rb.setChecked(True)
            self.checkstate()

    #to fetch saved data from database.
    def fetchteam(self,nam):
        self.query="SELECT * FROM team WHERE Team_name='{}';".format(nam)
        curcricket.execute(self.query)
        self.fteam=curcricket.fetchone()
        self.teamid=self.fteam[0]
        self.tname.setText(str(self.fteam[1]))
        self.pointavail.setText(str(self.fteam[2]))        
        self.bat.setText(str(self.fteam[3]))
        self.bow.setText(str(self.fteam[4]))
        self.ar.setText(str(self.fteam[6]))
        self.wk.setText(str(self.fteam[5]))
        self.point_avail=self.fteam[2]
        self.point_used=1000-self.point_avail
        self.pointused.setText(str(self.point_used))
        self.count_bat=self.fteam[3]
        self.count_bow=self.fteam[4]
        self.count_ar=self.fteam[6]
        self.count_wk=self.fteam[5]

        self.sql="SELECT * FROM teamplayer WHERE Team_id='{}';".format(self.teamid)
        curcricket.execute(self.sql)
        self.teamplayer_data=curcricket.fetchall()
        for plist in self.teamplayer_data:
            self.selectlist.addItem(str(plist[1]))

    #to check the state of radio button used
    def checkstate(self):
        if self.bat_rb.isChecked()==True:
            self.rb="BAT"
        if self.bow_rb.isChecked()==True:
            self.rb="BWL"
        if self.ar_rb.isChecked()==True:
            self.rb="AR"
        if self.wk_rb.isChecked()==True:
            self.rb="WK"

        self.playerlist.clear()
        if self.tname.text()!='Displayed Here':
            self.query="SELECT * FROM stats WHERE Category='{}';".format(self.rb)
            curcricket.execute(self.query)
            self.categ=curcricket.fetchall()
            for cat in self.categ:
                found = self.selectlist.findItems(cat[1],QtCore.Qt.MatchExactly)
                if found:
                    continue
                else:
                    self.playerlist.addItem(cat[1])
        else:
            self.showMessage("Team name","Team not found. \t\t\n Please select the team.")
            return
                    
    def __init__(self):
        self.count_bat = 0
        self.count_bow = 0
        self.count_ar = 0
        self.count_wk = 0
        self.point_avail = 1000
        self.point_used = 0
        self.removePL = []

    #to remove items from list1 and add them in list2.
    def changelist1(self):
        self.pcount=self.selectlist.count()
        if self.pcount < 11:
            self.play_name=self.playerlist.currentItem().text()
            self.play_row=self.playerlist.currentRow()
            self.query="SELECT * FROM stats WHERE Player_name='{}';".format(self.play_name)
            curcricket.execute(self.query)
            self.playerdata=curcricket.fetchone()
            
            if self.point_avail >= self.playerdata[6]:
                if self.playerdata[7] == "BAT":
                    self.count_bat += 1
                if self.playerdata[7] == "BWL":
                    self.count_bow += 1
                if self.playerdata[7] == "AR":
                    self.count_ar += 1
                if self.playerdata[7] == "WK":
                    if self.count_wk == 0:
                        self.count_wk = 1
                    else:
                        self.showMessage("Wicket-keeper","Only one wicket-keeper can be selected.")
                        return
                    
                self.point_avail -= self.playerdata[6]
                self.pointavail.setText(str(self.point_avail))
                self.point_used += self.playerdata[6]
                self.pointused.setText(str(self.point_used))
                
            else:
                self.showMessage("Error","You don't have enough points.")              
                return
            
            self.playerlist.takeItem(self.play_row)
            self.selectlist.addItem(self.play_name)
            self.bat.setText(str(self.count_bat))
            self.bow.setText(str(self.count_bow))
            self.ar.setText(str(self.count_ar))
            self.wk.setText(str(self.count_wk))
            
        else:
            self.showMessage("Message","You can't have more than 11 players in a team.")
            return
                          
    #to remove items from list2 and add them in list1.
    def changelist2(self):
        self.play_name=self.selectlist.currentItem().text()
        self.play_row=self.selectlist.currentRow()
        self.removePL.append(self.play_name)
        self.query="SELECT * FROM stats WHERE Player_name='{}';".format(self.play_name)
        curcricket.execute(self.query)
        self.playerdata=curcricket.fetchone()
            
        if self.playerdata[7] == "BAT":
            self.count_bat -= 1
        if self.playerdata[7] == "BWL":
            self.count_bow -= 1
        if self.playerdata[7] == "AR":
            self.count_ar -= 1
        if self.playerdata[7] == "WK":
            self.count_wk -= 1
                
        self.point_avail += self.playerdata[6]
        self.pointavail.setText(str(self.point_avail))
        self.point_used -= self.playerdata[6]
        self.pointused.setText(str(self.point_used))
            
        self.selectlist.takeItem(self.play_row)
        self.checkstate()
        self.bat.setText(str(self.count_bat))
        self.bow.setText(str(self.count_bow))
        self.ar.setText(str(self.count_ar))
        self.wk.setText(str(self.count_wk))
        
    #function for error message
    def showMessage(self,title,messag):
        msg=QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(messag)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    #function to save the team
    def saveteam(self):
        if self.tname.text()!='Displayed Here':
            for player in self.removePL:
                self.deletequery = "DELETE FROM teamplayer WHERE Team_id={} and Player_name='{}';".format(self.teamid,player)
                curcricket.execute(self.deletequery)
                cricket.commit()
            self.playersL2 = self.selectlist.findItems('*', QtCore.Qt.MatchWildcard)
            for player in self.playersL2:
                self.selectquery = "SELECT * FROM teamplayer WHERE Team_id={} and Player_name='{}';".format(self.teamid,player.text())
                curcricket.execute(self.selectquery)
                self.found = curcricket.fetchone()
                if self.found == None:
                    self.query = "INSERT INTO teamplayer (Team_id,Player_name) VALUES ({},'{}');".format(self.teamid,player.text())
                    curcricket.execute(self.query)
                    cricket.commit()

            self.pointdata = "update team set Value={}, Batsman={}, Bowler={}, Wicket_keeper={}, All_rounder={} where Team_id={};".format(self.point_avail,self.count_bat,self.count_bow,self.count_wk,self.count_ar,self.teamid)
            curcricket.execute(self.pointdata)
            cricket.commit()
        else:
            self.showMessage("Error","Select the team first.\t\t")
            return
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
