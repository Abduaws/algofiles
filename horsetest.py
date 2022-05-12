# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'horse.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 810)
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.go)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 651, 751))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.b1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b1.setFrameShape(QtWidgets.QFrame.Box)
        self.b1.setText("")
        self.b1.setAlignment(QtCore.Qt.AlignCenter)
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 3, 1, 1, 1)
        self.b2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b2.setFrameShape(QtWidgets.QFrame.Box)
        self.b2.setText("")
        self.b2.setAlignment(QtCore.Qt.AlignCenter)
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 2, 1, 1, 1)
        self.a4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.a4.setFrameShape(QtWidgets.QFrame.Box)
        self.a4.setText("")
        self.a4.setAlignment(QtCore.Qt.AlignCenter)
        self.a4.setObjectName("a4")
        self.gridLayout.addWidget(self.a4, 0, 0, 1, 1)
        self.b4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b4.setFrameShape(QtWidgets.QFrame.Box)
        self.b4.setText("")
        self.b4.setAlignment(QtCore.Qt.AlignCenter)
        self.b4.setObjectName("b4")
        self.gridLayout.addWidget(self.b4, 0, 1, 1, 1)
        self.b3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b3.setFrameShape(QtWidgets.QFrame.Box)
        self.b3.setText("")
        self.b3.setAlignment(QtCore.Qt.AlignCenter)
        self.b3.setObjectName("b3")
        self.gridLayout.addWidget(self.b3, 1, 1, 1, 1)
        self.a3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.a3.setFrameShape(QtWidgets.QFrame.Box)
        self.a3.setText("")
        self.a3.setAlignment(QtCore.Qt.AlignCenter)
        self.a3.setObjectName("a3")
        self.gridLayout.addWidget(self.a3, 1, 0, 1, 1)
        self.a1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.a1.setFrameShape(QtWidgets.QFrame.Box)
        self.a1.setText("")
        self.a1.setAlignment(QtCore.Qt.AlignCenter)
        self.a1.setObjectName("a1")
        self.gridLayout.addWidget(self.a1, 3, 0, 1, 1)
        self.c4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.c4.setFrameShape(QtWidgets.QFrame.Box)
        self.c4.setText("")
        self.c4.setAlignment(QtCore.Qt.AlignCenter)
        self.c4.setObjectName("c4")
        self.gridLayout.addWidget(self.c4, 0, 2, 1, 1)
        self.c2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.c2.setFrameShape(QtWidgets.QFrame.Box)
        self.c2.setText("")
        self.c2.setAlignment(QtCore.Qt.AlignCenter)
        self.c2.setObjectName("c2")
        self.gridLayout.addWidget(self.c2, 2, 2, 1, 1)
        self.c3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.c3.setFrameShape(QtWidgets.QFrame.Box)
        self.c3.setText("")
        self.c3.setAlignment(QtCore.Qt.AlignCenter)
        self.c3.setObjectName("c3")
        self.gridLayout.addWidget(self.c3, 1, 2, 1, 1)
        self.a2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.a2.setFrameShape(QtWidgets.QFrame.Box)
        self.a2.setText("")
        self.a2.setAlignment(QtCore.Qt.AlignCenter)
        self.a2.setObjectName("a2")
        self.gridLayout.addWidget(self.a2, 2, 0, 1, 1)
        self.c1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.c1.setFrameShape(QtWidgets.QFrame.Box)
        self.c1.setText("")
        self.c1.setAlignment(QtCore.Qt.AlignCenter)
        self.c1.setObjectName("label_12")
        self.gridLayout.addWidget(self.c1, 3, 2, 1, 1)
        self.next = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.next.setObjectName("next")
        self.gridLayout.addWidget(self.next, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setStyleSheet("background-color: grey;")
        self.curr_board = [["b", "b", "b"],
                           ["e", "e", "e"],
                           ["e", "e", "e"],
                           ["w", "w", "w"]]
        self.a1.setPixmap(
            QtGui.QPixmap('white.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
        self.b1.setPixmap(
            QtGui.QPixmap('white.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
        self.c1.setPixmap(
            QtGui.QPixmap('white.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
        self.a4.setPixmap(
            QtGui.QPixmap('black.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
        self.b4.setPixmap(
            QtGui.QPixmap('black.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
        self.c4.setPixmap(
            QtGui.QPixmap('black.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
        self.next.clicked.connect(lambda : self.div_solve(("a4", "black"), ("c4", "black")))
        self.white_pieces = ["a1", "b1", "c1"]
        self.black_pieces = ["a4", "b4", "c4"]
        self.moves = []
        self.go_index = 0
        self.next_flag = False
        self.turn = "white"
        self.timer.start()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next.setText(_translate("MainWindow", "NEXT"))
    def next_move(self):
        self.next_flag = True
    def go(self):
        if self.next_flag:
            self.a1.clear()
            self.a2.clear()
            self.a3.clear()
            self.a4.clear()
            self.b1.clear()
            self.b2.clear()
            self.b3.clear()
            self.b4.clear()
            self.c1.clear()
            self.c2.clear()
            self.c3.clear()
            self.c4.clear()
            self.a1.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.b1.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.c1.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.a4.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.b4.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.c4.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.next_flag = False
        else:
            if self.go_index == len(self.moves):
                self.timer.stop()
                self.go_index = 0
                return
            move = self.moves[self.go_index]
            self.swap_pieces((move[0], move[1]), move[2])
            self.go_index += 1
    def print_chess(self):
        print(f"  {'-' if self.a4.pixmap() is None else self.a4.pixmap()}   {'-' if self.a4.pixmap() is None else self.a4.pixmap()}   {'-' if self.a4.pixmap() is None else self.a4.pixmap()}\n"
              f"  {'-' if self.a4.pixmap() is None else self.a4.pixmap()}   {'-' if self.a4.pixmap() is None else self.a4.pixmap()}   {'-' if self.a4.pixmap() is None else self.a4.pixmap()}\n"
              f"  {'-' if self.a4.pixmap() is None else self.a4.pixmap()}   {'-' if self.a4.pixmap() is None else self.a4.pixmap()}   {'-' if self.a4.pixmap() is None else self.a4.pixmap()}\n"
              f"  {'-' if self.a4.pixmap() is None else self.a4.pixmap()}   {'-' if self.a4.pixmap() is None else self.a4.pixmap()}   {'-' if self.a4.pixmap() is None else self.a4.pixmap()}")
    def get_white_move(self):
        possible_a1 = ["b3", "c2"]
        possible_a2 = ["b4", "c3", "c1"]
        possible_a3 = ["b1", "c2", "c4"]
        possible_a4 = ["b2", "c3"]
        possible_b1 = ["a3", "c3"]
        possible_b2 = ["a4", "c4"]
        possible_b3 = ["a1", "c1"]
        possible_b4 = ["a2", "c2"]
        possible_c1 = ["a2", "b3"]
        possible_c2 = ["a1", "a3", "b4"]
        possible_c3 = ["a2", "a4", "b1"]
        possible_c4 = ["a3", "b2"]
        white_pick = random.choice(self.white_pieces)
        possible_white = []
        if white_pick == "a1":
            possible_white = possible_a1
            self.a1.clear()
        elif white_pick == "a2":
            possible_white = possible_a2
            self.a2.clear()
        elif white_pick == "a3":
            possible_white = possible_a3
            self.a3.clear()
        elif white_pick == "a4":
            possible_white = possible_a4
            self.a4.clear()
        elif white_pick == "b1":
            possible_white = possible_b1
            self.b1.clear()
        elif white_pick == "b2":
            possible_white = possible_b2
            self.b2.clear()
        elif white_pick == "b3":
            possible_white = possible_b3
            self.b3.clear()
        elif white_pick == "b4":
            possible_white = possible_b4
            self.b4.clear()
        elif white_pick == "c1":
            possible_white = possible_c1
            self.c1.clear()
        elif white_pick == "c2":
            possible_white = possible_c2
            self.c2.clear()
        elif white_pick == "c3":
            possible_white = possible_c3
            self.c3.clear()
        elif white_pick == "c4":
            possible_white = possible_c4
            self.c4.clear()
        move_white = random.choice(possible_white)
        counter = 0
        while move_white in self.black_pieces or move_white in self.white_pieces:
            if counter>20:return white_pick, white_pick
            move_white = random.choice(possible_white)
            counter+=1
        if move_white == "a1":
            self.a1.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "a2":
            self.a2.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.a2.width(), self.a2.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "a3":
            self.a3.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.a3.width(), self.a3.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "a4":
            self.a4.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.a4.width(), self.a4.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "b1":
            self.b1.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.b1.width(), self.b1.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "b2":
            self.b2.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.b2.width(), self.b2.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "b3":
            self.b3.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.b3.width(), self.b3.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "b4":
            self.b4.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.b4.width(), self.b4.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "c1":
            self.c1.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.c1.width(), self.c1.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "c2":
            self.c2.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.c2.width(), self.c2.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "c3":
            self.c3.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.c3.width(), self.c3.height(), QtCore.Qt.KeepAspectRatio))
        elif move_white == "c4":
            self.c4.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.c4.width(), self.c4.height(), QtCore.Qt.KeepAspectRatio))
        return white_pick, move_white
    def get_black_move(self):
        possible_a1 = ["b3", "c2"]
        possible_a2 = ["b4", "c3", "c1"]
        possible_a3 = ["b1", "c2", "c4"]
        possible_a4 = ["b2", "c3"]
        possible_b1 = ["a3", "c3"]
        possible_b2 = ["a4", "c4"]
        possible_b3 = ["a1", "c1"]
        possible_b4 = ["a2", "c2"]
        possible_c1 = ["a2", "b3"]
        possible_c2 = ["a1", "a3", "b4"]
        possible_c3 = ["a2", "a4", "b1"]
        possible_c4 = ["a3", "b2"]
        black_pick = random.choice(self.black_pieces)
        possible_black = []
        if black_pick == "a1":
            possible_black = possible_a1
            self.a1.clear()
        elif black_pick == "a2":
            possible_black = possible_a2
            self.a2.clear()
        elif black_pick == "a3":
            possible_black = possible_a3
            self.a3.clear()
        elif black_pick == "a4":
            possible_black = possible_a4
            self.a4.clear()
        elif black_pick == "b1":
            possible_black = possible_b1
            self.b1.clear()
        elif black_pick == "b2":
            possible_black = possible_b2
            self.b2.clear()
        elif black_pick == "b3":
            possible_black = possible_b3
            self.b3.clear()
        elif black_pick == "b4":
            possible_black = possible_b4
            self.b4.clear()
        elif black_pick == "c1":
            possible_black = possible_c1
            self.c1.clear()
        elif black_pick == "c2":
            possible_black = possible_c2
            self.c2.clear()
        elif black_pick == "c3":
            possible_black = possible_c3
            self.c3.clear()
        elif black_pick == "c4":
            possible_black = possible_c4
            self.c4.clear()
        move_black = random.choice(possible_black)
        counter = 0
        while move_black in self.black_pieces or move_black in self.white_pieces:
            if counter>20:return black_pick, black_pick
            move_black = random.choice(possible_black)
            counter+=1
        if move_black == "a1":
            self.a1.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "a2":
            self.a2.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.a2.width(), self.a2.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "a3":
            self.a3.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.a3.width(), self.a3.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "a4":
            self.a4.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.a4.width(), self.a4.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "b1":
            self.b1.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.b1.width(), self.b1.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "b2":
            self.b2.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.b2.width(), self.b2.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "b3":
            self.b3.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.b3.width(), self.b3.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "b4":
            self.b4.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.b4.width(), self.b4.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "c1":
            self.c1.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.c1.width(), self.c1.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "c2":
            self.c2.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.c2.width(), self.c2.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "c3":
            self.c3.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.c3.width(), self.c3.height(), QtCore.Qt.KeepAspectRatio))
        elif move_black == "c4":
            self.c4.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.c4.width(), self.c4.height(), QtCore.Qt.KeepAspectRatio))
        return black_pick, move_black
    def swap_pieces(self, first_piece, second_piece):
        if first_piece[0] == "a1": self.a1.clear()
        elif first_piece[0] == "a2": self.a2.clear()
        elif first_piece[0] == "a3": self.a3.clear()
        elif first_piece[0] == "a4": self.a4.clear()
        elif first_piece[0] == "b1": self.b1.clear()
        elif first_piece[0] == "b2": self.b2.clear()
        elif first_piece[0] == "b3": self.b3.clear()
        elif first_piece[0] == "b4": self.b4.clear()
        elif first_piece[0] == "c1": self.c1.clear()
        elif first_piece[0] == "c2": self.c2.clear()
        elif first_piece[0] == "c3": self.c3.clear()
        elif first_piece[0] == "c4": self.c4.clear()
        url = f'{first_piece[1]}.png'
        if second_piece == "a1":self.a1.setPixmap(QtGui.QPixmap(url).scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "a2":self.a2.setPixmap(QtGui.QPixmap(url).scaled(self.a2.width(), self.a2.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "a3":self.a3.setPixmap(QtGui.QPixmap(url).scaled(self.a3.width(), self.a3.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "a4":self.a4.setPixmap(QtGui.QPixmap(url).scaled(self.a4.width(), self.a4.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "b1":self.b1.setPixmap(QtGui.QPixmap(url).scaled(self.b1.width(), self.b1.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "b2":self.b2.setPixmap(QtGui.QPixmap(url).scaled(self.b2.width(), self.b2.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "b3":self.b3.setPixmap(QtGui.QPixmap(url).scaled(self.b3.width(), self.b3.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "b4":self.b4.setPixmap(QtGui.QPixmap(url).scaled(self.b4.width(), self.b4.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "c1":self.c1.setPixmap(QtGui.QPixmap(url).scaled(self.c1.width(), self.c1.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "c2":self.c2.setPixmap(QtGui.QPixmap(url).scaled(self.c2.width(), self.c2.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "c3":self.c3.setPixmap(QtGui.QPixmap(url).scaled(self.c3.width(), self.c3.height(), QtCore.Qt.KeepAspectRatio))
        elif second_piece == "c4":self.c4.setPixmap(QtGui.QPixmap(url).scaled(self.c4.width(), self.c4.height(), QtCore.Qt.KeepAspectRatio))
        self.not_stop_flag = True
    def solve(self):
        self.div_solve(("a4", "black"), ("c4", "black"))
    def div_solve(self, first_piece:tuple, second_piece:tuple):
        if first_piece[0] == "a4" and first_piece[1] == "black" and second_piece[0] == "c4" and second_piece[1] == "black":
            # swap a4 -> c3
            self.moves.append(("a4", "black", "c3"))
            # swap c4 -> a3
            self.moves.append(("c4", "black", "a3"))
            # swap a3 -> c2
            self.moves.append(("a3", "black", "c2"))
            self.div_solve(("c3", "black"), ("b1", "white"))
        elif first_piece[0] == "c3" and first_piece[1] == "black" and second_piece[0] == "b1" and second_piece[1] == "white":
            # swap b1 -> a3
            self.moves.append(("b1", "white", "a3"))
            # swap a3 -> c4
            self.moves.append(("a3", "white", "c4"))
            # swap c3 -> b1
            self.moves.append(("c3", "black", "b1"))
            self.div_solve(("c2", "black"), ("c1", "white"))
        elif first_piece[0] == "c2" and first_piece[1] == "black" and second_piece[0] == "c1" and second_piece[1] == "white":
            # swap c2 -> a3
            self.moves.append(("c2", "black", "a3"))
            # swap c1 -> a2
            self.moves.append(("c1", "white", "a2"))
            # swap a2 -> c3
            self.moves.append(("a2", "white", "c3"))
            self.div_solve(("b4", "black"), ("a1", "white"))
        elif first_piece[0] == "b4" and first_piece[1] == "black" and second_piece[0] == "a1" and second_piece[1] == "white":
            # swap a1 -> c2
            self.moves.append(("a1", "white", "c2"))
            # swap b4 -> a2
            self.moves.append(("b4", "black", "a2"))
            self.div_solve(("c2", "white"), ("c3", "white"))
        elif first_piece[0] == "c2" and first_piece[1] == "white" and second_piece[0] == "c3" and second_piece[1] == "white":
            # swap c2 -> b4
            self.moves.append(("c2", "white", "b4"))
            # swap c3 -> a4
            self.moves.append(("c3", "white", "a4"))
            self.div_solve(("a2", "black"), ("a3", "black"))
        elif first_piece[0] == "a2" and first_piece[1] == "black" and second_piece[0] == "a3" and second_piece[1] == "black":
            # swap a2 -> c1
            self.moves.append(("a2", "black", "c1"))
            # swap a3 -> c2
            self.moves.append(("a3", "black", "c2"))
            # swap c2 -> a1
            self.moves.append(("c2", "black", "a1"))
            self.a1.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.b1.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.c1.setPixmap(
                QtGui.QPixmap('white.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.a4.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.b4.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.c4.setPixmap(
                QtGui.QPixmap('black.png').scaled(self.a1.width(), self.a1.height(), QtCore.Qt.KeepAspectRatio))
            self.timer.start()
            return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
