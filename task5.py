import copy
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 837)
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.show_zolution)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputnodes = QtWidgets.QLineEdit(self.centralwidget)
        self.inputnodes.setGeometry(QtCore.QRect(480, 680, 113, 22))
        self.inputnodes.setObjectName("inputnodes")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(440, 720, 93, 28))
        self.add.setObjectName("add")
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
        self.reset.clicked.connect(lambda :self.printt())
        self.add.clicked.connect(self.draw)
        self.inputnodes.returnPressed.connect(lambda : self.draw())
        self.steps = 0
        self.arr = []
        self.shortest_steps = []
        self.show_index = 0
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def printt(self):
        self.stepbystep(self.arr, 0, len(self.arr)-1)
        self.timer.start()
    def draw(self):
        self.steps = 0
        self.arr = []
        self.shortest_steps = []
        self.show_index = 0
        self.plainTextEdit.clear()
        if self.inputnodes.text() == "": return
        n = self.inputnodes.text()
        self.arr = ["1"]*int(n)
        self.plainTextEdit.setPlainText(str(self.arr))
    def stepbystep(self, arr:list, start, end):
        if end - start == 0:
            arr[start] = "0"
            self.shortest_steps.append(copy.deepcopy(self.arr))
            print(arr[start:start + 2], end=" ")
            print(arr[start + 2:len(arr)])
            return
        if end == start + 1:
            arr[start] = "0"
            print(arr[start:start + 2], end=" ")
            print(arr[start + 2:len(arr)])
            self.shortest_steps.append(copy.deepcopy(self.arr))
            arr[end] = "0"
            self.shortest_steps.append(copy.deepcopy(self.arr))
            print(arr[start:start + 2], end=" ")
            print(arr[start + 2:len(arr)])
            return
        self.stepbystep(arr, start + 2, len(arr) - 1)
        self.stepbystep(arr, start, start+1)
    def show_zolution(self):
        if self.show_index == len(self.shortest_steps):
            self.timer.stop()
            self.show_index = 0
            return
        self.arr = self.shortest_steps[self.show_index]
        self.plainTextEdit.setPlainText(str(self.arr))
        self.show_index += 1
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
        self.reset.setText(_translate("MainWindow", "Solve"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
