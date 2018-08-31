from threading import Lock

from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout
from PyQt5.QtCore import pyqtSignal, QObject


class Signals(QObject):
    render = pyqtSignal()


class Window(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        
        self.lock = Lock()
        self.labels = []
        self.buffer = []
        self.signals = Signals()
        self.layout = QGridLayout()

        self.setWindowTitle('EasyClipboard')
        self.resize(width, height)
        self.setLayout(self.layout)
        self.signals.render.connect(self.show_normal)
    
    def show_window(self, x, y):
        # TODO: получать координаты указателя перед вызовом этой функции 
        self.move(x, y)
        self.show()

    def show_minimized(self):
        self.showMinimized()

    def show_normal(self):
        self.showNormal()
        with self.lock:
            print(self.buffer)
            buffer_length = len(self.buffer)
            labels_length = len(self.labels)
            if (buffer_length > labels_length):
                for i in range(labels_length, buffer_length):
                    print(i, self.buffer[i])
                    label = QLabel(self.buffer[i], self)
                    #label.move(10, 20 * i)
                    self.layout.addWidget(label, i, 1, 1, 1)
                    ###
                    self.labels.append(label)
