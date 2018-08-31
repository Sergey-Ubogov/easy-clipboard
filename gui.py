from threading import Lock

from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, QObject, Qt, QEvent


# TODO: посмотреть как будет выглядеть select
# TODO: пофиксить обрытный порядок выбора кнопок
class Label(QPushButton):
    def __init__(self, text: str, parent: QWidget):
        super().__init__(text, parent)
        self.setStyleSheet("color:#eeeeee;")


class Window(QMainWindow):

    render_signal = pyqtSignal(int, int)
    add_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        centralWidget = QWidget()
        centralWidget.setStyleSheet("background-color:#222222;")
        self.lock = Lock()
        self.labels = []
        self.layout = QVBoxLayout()

        self.setWindowFlag(Qt.FramelessWindowHint)
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)
        self.render_signal.connect(self.render)
        self.add_signal.connect(self.add_label)

    def render(self, x: int, y: int):
        for label in self.labels: 
            self.layout.removeWidget(label)
        with self.lock:
            self.labels = self.labels[:15]
            for label in self.labels:
                self.layout.addWidget(label)
        self.move(x, y)
        self.show()

    def add_label(self, text: str):
        new_label = Label(text, self)
        with self.lock:
            self.labels.insert(0, new_label)
