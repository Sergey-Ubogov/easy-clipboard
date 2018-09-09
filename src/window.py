from threading import Lock
import sys
from os import path

from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView, \
    QStyle, QSystemTrayIcon, QAction, QMenu, QStyle
from PyQt5.QtCore import pyqtSignal, QObject, Qt, QSize
from PyQt5.QtGui import QIcon
from logic import imitate_paste
from autoload import managament_startup, get_startup_file_name

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

        self.setToTray();

    def setAutoloadText(self):
        if (path.exists(get_startup_file_name())):
            self.autoload_action.setText('Убрать из автозагрузки')
        else:
            self.autoload_action.setText('Добавить в автозагрузку')

    def startup_action(self, checked):
        managament_startup()
        self.setAutoloadText()

    def quit_action(self, checked):
        self.clear()
        self.hide()
        self.close()

    def setToTray(self):
        self.tray_icon = QSystemTrayIcon(self)

        self.tray_icon.setIcon(self.style().standardIcon(56))
        
        self.autoload_action = QAction("Добавить в автозагрузку", self)
        self.setAutoloadText()

        quit_action = QAction("Выход", self)
        
        self.autoload_action.triggered.connect(self.startup_action)
        quit_action.triggered.connect(self.quit_action)

        tray_menu = QMenu()
        tray_menu.addAction(self.autoload_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

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
        self.activateWindow()

    def add_label(self, text: str):
        with self.lock:
            self.buffer.insert(0, text)

    def item_changed(self):
        self.hide()
        imitate_paste(self.currentItem().text())
