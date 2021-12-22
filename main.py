import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(250, 250, 210))
            r = random.randint(0, 100)
            qp.drawEllipse(random.randint(r, 497 - r), random.randint(r, 495 - r), r, r)
            qp.end()

    def draw(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())