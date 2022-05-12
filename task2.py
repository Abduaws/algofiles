import copy
from PyQt5 import QtCore, QtGui, QtWidgets


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
            self.plainTextEdit.clear()
            if self.inputnodes.text() == "": return
            n = self.inputnodes.text()
            options = n.split(",")
            self.arr = ["♚"] * int(options[0])
            self.arr[int(options[1])] = "-"
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
    def stepbystep(self):
        flag = True
        indexes = [index for index, value in enumerate(self.arr) if value == "♚"]
        for indic in range(1, len(indexes)):
            if abs(indexes[0] - indexes[indic]) % 2 != 0:
                flag = False
            if flag:
                print("failed")
        if self.arr.count("♚") == 1:
            f = open("res.txt", 'a')
            f.write(f"{self.first},{self.second}   |   Steps: {self.steps}\n")
            self.timer.start()
            return
        choice = []
        for index in range(0, len(self.arr)):
            if index == len(self.arr):
                break
            if self.arr[index] == "-":
                if index-2 >= 0:
                    if self.arr[index-2] == "♚" and self.arr[index-1] == "♚":
                        choice.append((index-2, index-1, index, abs(int((len(self.arr)-1)/2)-index-2)))
                if index+2 <= len(self.arr)-1:
                    if self.arr[index+2] == "♚" and self.arr[index+1] == "♚":
                        choice.append((index+2, index+1, index, abs(int((len(self.arr)-1)/2)-index-2)))
        print("Current Choices: ", choice)
        if choice:
            curr_min = tuple()
            mid = int((len(self.arr)-1)/2)
            min_abs = 9999999
            for option in choice:
                print("Current Choice: ", option)
                if self.arr.count("♚") > 2:
                    indexes = [index for index, value in enumerate(self.arr) if value == "♚" and index != option[0] and index != option[1]]
                    flag = True
                    for indic in indexes:
                        if abs(option[2] - indic) % 2 != 0:
                            flag = False
                    if flag: continue
                diff = abs(option[0]-mid)
                if diff < min_abs :
                    min_abs = diff
                    curr_min = option
                print("Current Min: ", curr_min)
            if not curr_min: curr_min = choice[0]
            self.arr[curr_min[0]] = "-"
            self.arr[curr_min[1]] = "-"
            self.arr[curr_min[2]] = "♚"
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
