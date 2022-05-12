import copy
from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 837)
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.show_steps)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputnodes = QtWidgets.QLineEdit(self.centralwidget)
        self.inputnodes.setGeometry(QtCore.QRect(480, 680, 113, 22))
        self.inputnodes.setObjectName("inputnodes")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(440, 720, 93, 28))
        self.add.setObjectName("add")
        self.outputbtn = QtWidgets.QPushButton(self.centralwidget)
        self.outputbtn.setGeometry(QtCore.QRect(20, 350, 93, 28))
        self.outputbtn.setObjectName("outputbtn")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(540, 720, 93, 28))
        self.reset.setObjectName("reset")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 20, 811, 651))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.reset.clicked.connect(self.stepbystep)
        self.add.clicked.connect(self.draw)
        self.inputnodes.returnPressed.connect(lambda : self.draw(True))
        self.outputbtn.clicked.connect(self.outputfile)
        self.steps = 0
        self.flag = True
        self.arr = []
        self.move_parent = dict()
        self.moves = []
        self.outputflag = False
        self.shortest_steps = []
        self.show_index = 0
        self.first = ""
        self.second = ""
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def show_steps(self):
        if self.show_index == len(self.shortest_steps):
            self.timer.stop()
            self.show_index = 0
            self.popup()
            return
        self.arr = self.shortest_steps[self.show_index]
        self.printt()
        self.show_index += 1
    def outputfile(self):
        self.outputflag = True
        for first in range(4, 100, 2):
            for second in range(0, first):
                self.first = first
                self.second = second
                self.inputnodes.setText(str(first)+","+str(second))
                self.draw()
                self.stepbystep()
        self.outputflag = False
    def printt(self):
        self.plainTextEdit.setPlainText(str(self.arr))
    def draw(self, flag = False):
        if flag:
            self.steps = 0
            self.arr = []
            self.shortest_steps = []
            self.show_index = 0
            self.moves = []
            self.plainTextEdit.clear()
            if self.inputnodes.text() == "": return
            n = self.inputnodes.text()
            options = n.split(",")
            self.arr = ["♚"] * int(options[0])
            self.arr[int(options[1])] = "-"
            self.moves.append(self.arr)
            print("In draw loop: ", self.arr)
            self.printt()
            self.stepbystep()
            return
        self.steps = 0
        self.arr = []
        self.shortest_steps = []
        self.show_index = 0
        self.plainTextEdit.clear()
        if self.inputnodes.text() == "": return
        n = self.inputnodes.text()
        options = n.split(",")
        self.arr = ["♚"]*int(options[0])
        self.arr[int(options[1])] = "-"
        print("In draw loop: ", self.arr)
        self.printt()
    def errpopup(self, msg):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setWindowIcon(QtGui.QIcon("icon.png"))
        msg.setText(msg)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        x = msg.exec_()
    def check_fail(self, fl = False, arr=[]):
        if fl:
            flag = True
            failflag = True
            indexes = [index for index in range(0, len(arr)) if arr[index] == "♚"]
            for index in range(0, len(indexes)):
                for indic in range(index + 1, len(indexes)):
                    if abs(indexes[index] - indexes[indic]) == 1:
                        failflag = False
                    if abs(indexes[index] - indexes[indic]) % 2 != 0:
                        flag = False
            return flag, failflag
        flag = True
        failflag = True
        indexes = [index for index in range(0, len(self.arr)) if self.arr[index] == "♚"]
        for index in range(0, len(indexes)):
            for indic in range(index + 1, len(indexes)):
                if abs(indexes[index] - indexes[indic]) == 1:
                    failflag = False
                if abs(indexes[index] - indexes[indic]) % 2 != 0:
                    flag = False
        return flag, failflag
    def stepbystep(self):
        if self.arr.count("♚") == 1:
            f = open("res.txt", 'a')
            f.write(f"{self.first},{self.second}   |   Steps: {self.steps}\n")
            self.timer.start()
            return
        flags = self.check_fail()
        if flags[0] or flags[1]:
            print("failed")
            return
        for index in range(0, len(self.arr)):
            print("Curr Index", index)
            left_flag = False
            right_flag = False
            if index+2 < len(self.arr):
                if self.arr[index] == "-" and self.arr[index + 1] == "♚" and self.arr[index + 2] == "♚":
                    left_flag = True
            if index-2 >= 0:
                if self.arr[index] == "-" and self.arr[index - 1] == "♚" and self.arr[index - 2] == "♚":
                    right_flag = True
            if right_flag and left_flag:
                if abs(index+2-((len(self.arr)/2)-1)) < abs(index-2-((len(self.arr)/2)-1)):
                    self.arr[index] = "♚"
                    self.arr[index + 1] = "-"
                    self.arr[index + 2] = "-"
                    self.steps += 1
                    self.shortest_steps.append(copy.deepcopy(self.arr))
                    print("In loop: ", self.arr)
                elif abs(index+2-((len(self.arr)/2)-1)) > abs(index-2-((len(self.arr)/2)-1)):
                    self.arr[index] = "♚"
                    self.arr[index - 1] = "-"
                    self.arr[index - 2] = "-"
                    self.steps += 1
                    self.shortest_steps.append(copy.deepcopy(self.arr))
                    print("In loop: ", self.arr)
                else:
                    choice = random.choice([0,1])
                    if choice == 0:
                        #print(self.arr[index - 2], self.arr[index - 1], self.arr[index])
                        self.arr[index] = "♚"
                        self.arr[index - 1] = "-"
                        self.arr[index - 2] = "-"
                        self.steps += 1
                        self.shortest_steps.append(copy.deepcopy(self.arr))
                        print("right chosen")
                        print("In loop: ", self.arr)
                    else:
                        #print(self.arr[index], self.arr[index + 1], self.arr[index + 2])
                        self.arr[index] = "♚"
                        self.arr[index + 1] = "-"
                        self.arr[index + 2] = "-"
                        self.steps += 1
                        self.shortest_steps.append(copy.deepcopy(self.arr))
                        print("left chosen")
                        print("In loop: ", self.arr)
            elif right_flag:
                #print(self.arr[index - 2], self.arr[index - 1], self.arr[index])
                self.arr[index] = "♚"
                self.arr[index - 1] = "-"
                self.arr[index - 2] = "-"
                self.steps += 1
                self.shortest_steps.append(copy.deepcopy(self.arr))
                print("In loop: ", self.arr)
            elif left_flag:
                #print(self.arr[index], self.arr[index + 1], self.arr[index + 2])
                self.arr[index] = "♚"
                self.arr[index + 1] = "-"
                self.arr[index + 2] = "-"
                self.steps += 1
                self.shortest_steps.append(copy.deepcopy(self.arr))
                print("In loop: ", self.arr)
        self.stepbystep()
    def popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Done")
        msg.setWindowIcon(QtGui.QIcon("icon.png"))
        msg.setText("Clear But One Done!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setInformativeText("Problem was solved in "+str(self.steps)+" steps!")
        x = msg.exec_()
        self.shortest_steps = []
        self.steps = 0
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Problem Solver"))
        self.add.setText(_translate("MainWindow", "Draw"))
        self.outputbtn.setText(_translate("MainWindow", "OutputFile"))
        self.reset.setText(_translate("MainWindow", "Solve"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
