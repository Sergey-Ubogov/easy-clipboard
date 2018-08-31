#!/usr/bin/env python3
import sys

import keyboard
import win32gui
import clipboard
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread

from gui import Window

WINDOW = None


class KeyboardHandler(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        keyboard.add_hotkey('ctrl+c', read_clipboard) 
        keyboard.add_hotkey('ctrl+shift+v', show_buffer, suppress=True)
        keyboard.wait()


def read_clipboard():
    data = clipboard.paste()
    with WINDOW.lock:
        WINDOW.add_signal.emit(data)


def show_buffer():
    x,y = win32gui.GetCursorInfo()[2]
    WINDOW.render_signal.emit(x, y)


def start_gui():
    global WINDOW
    app = QApplication(sys.argv)
    WINDOW = Window()
    app.exec_()


def main():
    keyboard_hangler = KeyboardHandler()
    keyboard_hangler.start()
    start_gui()

if __name__ == '__main__':
    main()