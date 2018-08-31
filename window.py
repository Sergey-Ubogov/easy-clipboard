from threading import Lock

import keyboard
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView
from PyQt5.QtCore import pyqtSignal, QObject, Qt, QSize

from logic import imitate_paste


class Window(QListWidget):

    render_signal = pyqtSignal(int, int)
    add_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#222;color:#eee;")
        self.lock = Lock()
        self.buffer = []

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.render_signal.connect(self.render)
        self.add_signal.connect(self.add_label)
        self.itemClicked.connect(self.item_changed)
        self.itemActivated.connect(self.item_changed)
        self.focusOutEvent = self.onFocusOutEvent

    def onFocusOutEvent(self, event):
        super().focusOutEvent(event)
        self.hide()

    def render(self, x: int, y: int):
        self.clear()
        with self.lock:
            self.buffer = self.buffer[:15]
            for text in self.buffer:
                self.addItem(text)
        self.move(x, y)
        self.show()

    def add_label(self, text: str):
        with self.lock:
            self.buffer.insert(0, text)

    def item_changed(self):
        self.hide()
        imitate_paste(self.currentItem().text())
