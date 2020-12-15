# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EVALUATE_Team.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
cricket=sqlite3.connect('Fantacycricket.db')
curcricket=cricket.cursor()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(708, 565)
        Form.setMinimumSize(QtCore.QSize(708, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(70, 8, 70, 8)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_1 = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.cb_1.setFont(font)
        self.cb_1.setObjectName("cb_1")
        self.horizontalLayout.addWidget(self.cb_1)
        self.cb_2 = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.cb_2.setFont(font)
        self.cb_2.setObjectName("cb_2")
        self.horizontalLayout.addWidget(self.cb_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(50, 20, 50, 0)
        self.horizontalLayout_3.setSpacing(70)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.score = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.score.setFont(font)
        self.score.setStyleSheet("color: rgb(0, 170, 255);")
        self.score.setText("")
        self.score.setObjectName("score")
        self.horizontalLayout_4.addWidget(self.score)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_2.setSpacing(70)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listplayername = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.listplayername.setFont(font)
        self.listplayername.setObjectName("listplayername")
        self.horizontalLayout_2.addWidget(self.listplayername)
        self.listpoint = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.listpoint.setFont(font)
        self.listpoint.setStyleSheet("color: rgb(0, 170, 255);")
        self.listpoint.setObjectName("listpoint")
        self.horizontalLayout_2.addWidget(self.listpoint)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.showdetails()
        self.cb_1.currentIndexChanged.connect(self.playerdata)
        self.cb_2.currentIndexChanged.connect(self.scoredata)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Evaluate Team"))
        self.label.setText(_translate("Form", "Evaluate the Performance of your Fantasy Team"))
        self.label_3.setText(_translate("Form", "Players"))
        self.label_2.setText(_translate("Form", "Points"))


    def batting(self,player):
        self.points = 0
        self.strike = 0
        self.points = player[2]//2
        if player[2] >= 50:
            self.points += 5
        if player[2] >= 100:
            self.points += 10

        if player[3] != 0:
            self.strike = (player[2]*100)/player[3]
            if self.strike >= 80 and self.strike <= 100:
                self.points += 2
            if self.strike > 100:
                self.points +=4
            
        self.points += player[4]
        self.points += 2 * player[5]
        return self.points


    def bowling(self,player):
        self.points = 0
        self.economy = 0
        self.over = 0
        self.points = 10 * player[9]
        if player[9] == 3:
            self.points += 5
        if player[9] >= 5:
            self.points += 10

        self.over = (player[6]/6)
        if self.over != 0:
            self.economy = player[8]/self.over
            if self.economy >= 3.5 and self.economy <= 4.5:
                self.points += 4   
            if self.economy >= 2 and self.economy <= 3.5:
                self.points += 7
            if self.economy < 2:
                self.points += 10
        return self.points

    def fielding(self,player):
        self.points = 0
        self.points = 10*(player[10] + player[11] + player[12])
        return self.points

    def showdetails(self):
        self.cb_1.addItem("Select Team")
        self.query = "SELECT * FROM team"
        curcricket.execute(self.query)
        self.data = curcricket.fetchall()
        for players in self.data:
            self.cb_1.addItem(str(players[1]))

        self.matchL = ["Select Match", "Match 1", "Match 2"]
        for match_ in self.matchL:
            self.cb_2.addItem(match_)
        

    def playerdata(self):
        self.listplayername.clear()
        self.listpoint.clear()
        self.score.clear()
        self.team_name = self.cb_1.currentText()
        self.cb_2.setCurrentText("Select Match")
        
        self.query = "SELECT * FROM team INNER JOIN teamplayer ON team.Team_id = teamplayer.Team_id WHERE team.Team_name = '{}';".format(self.team_name)
        curcricket.execute(self.query)
        self.player_data = curcricket.fetchall()
        for player in self.player_data:
            self.listplayername.addItem(str(player[8]))


    def scoredata(self):
        self.totalscore = 0
        self.listpoint.clear()
        
        self.match_num = self.cb_2.currentText()
        if self.match_num != "Select Match":
            if self.match_num == "Match 1":
                self.matchid = 1
            if self.match_num == "Match 2":
                self.matchid = 2
            
            for player in self.player_data:
                self.player_score = 0
                self.query = "SELECT * FROM match INNER JOIN stats ON match.Player_id = stats.Player_id WHERE stats.Player_name = '{}' and match.Match_id = {};".format(player[8],self.matchid)
                curcricket.execute(self.query)
                self.matchdata = curcricket.fetchone()
                self.player_score += self.batting(self.matchdata)
                self.player_score += self.bowling(self.matchdata)
                self.player_score += self.fielding(self.matchdata)
                self.totalscore += self.player_score
                self.listpoint.addItem(str(self.player_score))
                self.score.setText(str(self.totalscore))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
