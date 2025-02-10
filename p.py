import sys
from random import randint
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor, QPaintEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled1.ui', self)
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
        qp.setPen(QColor('yellow'))
        qp.setBrush(QColor('yellow'))
        circles = []
        while len(circles) < 3:
            radius = randint(10, 80)
            x = randint(0 + radius, self.centralwidget.width() - radius)
            y = randint(0 + radius, self.centralwidget.height() - radius)
            if not any(self.not_overlay(x, y, radius, circle) for circle in
                       circles):
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