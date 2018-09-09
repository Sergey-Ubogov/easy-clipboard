import keyboard
from PyQt5.QtCore import QThread

from window import Window
from logic import show_buffer, read_clipboard


class KeyboardHandler(QThread):
    def __init__(self, window: Window):
        QThread.__init__(self)
        self.window = window

    def copy_handler(self):
        read_clipboard(self.window)

    def insert_handler(self):
        show_buffer(self.window)

    def __del__(self):
        self.wait()

    def run(self):
        keyboard.add_hotkey('ctrl+c', self.copy_handler) 
        keyboard.add_hotkey('ctrl+shift+v', self.insert_handler, suppress=True)
        keyboard.wait()
