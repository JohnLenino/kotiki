import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtCore import Qt
from template import Ui_MainWindow as Tem


class CircleWidget(QMainWindow, Tem):
    def __init__(self):
        super(CircleWidget, self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.pushButton.clicked.connect(self.add_circles)

    def add_circles(self):
        num_circles = random.randint(1, 10)
        self.scene.clear()
        for _ in range(num_circles):
            diameter = random.randint(20, 100)
            color = QColor(Qt.yellow)

            ellipse = QGraphicsEllipseItem(0, 0, diameter, diameter)
            ellipse.setBrush(QBrush(color))

            x = random.randint(0, self.graphicsView.width() - diameter)
            y = random.randint(0, self.graphicsView.height() - diameter)

            ellipse.setPos(x, y)

            self.scene.addItem(ellipse)

def except_hooks(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWidget()
    window.setWindowTitle('Окружности PyQt5')
    window.setGeometry(100, 100, 800, 800)
    window.show()
    sys.excepthook = except_hooks
    sys.exit(app.exec_())
