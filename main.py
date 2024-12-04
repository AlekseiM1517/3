import sys
from PyQt6 import QtWidgets, uic
import random
from PyQt6.QtGui import QPainter, QColor


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.create_circle)

    def create_circle(self):
        diameter = random.randint(10, 100)
        color = QColor(255, 255, 0)
        circle = Circle(self, diameter, color)
        circle.move(random.randint(10, 300), random.randint(10, 300))
        circle.show()


class Circle(QtWidgets.QLabel):
    def __init__(self, parent, diameter, color):
        super(Circle, self).__init__(parent)
        self.setFixedSize(diameter, diameter)
        self.color = color

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.color)
        painter.drawEllipse(0, 0, self.width(), self.height())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
