import sys
from random import randint
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QFont, QPaintEvent, QPainter, QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 510, 281, 41))
        font = QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git и желтые окружности"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать окружности"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.painting = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.painting = True
        self.repaint()

    def paintEvent(self, event: QPaintEvent):
        if self.painting:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp: QPainter):
        colors = [QColor(randint(0, 255), randint(0, 255), randint(0, 255)) for i in range(3)]
        circles = []
        while len(circles) < 3:
            radius = randint(10, 80)
            x = randint(0 + radius, self.centralwidget.width() - radius)
            y = randint(0 + radius, self.centralwidget.height() - radius)
            if not any(self.not_overlay(x, y, radius, circle) for circle in
                       circles):
                color = colors[len(circles)]
                qp.setPen(color)
                qp.setBrush(color)
                circles.append((x, y, radius))
                qp.drawEllipse(x - radius, y - radius, radius * 2, radius * 2)

    def not_overlay(self, x, y, radius, circle):
        circle_x, circle_y, circle_radius = circle
        distance = (circle_x - x) ** 2 + (circle_y - y) ** 2
        return distance < (circle_radius + radius) ** 2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
