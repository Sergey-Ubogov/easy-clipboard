#!/usr/bin/env python3
import sys

import clipboard
import keyboard
#import win32gui
from PyQt5.QtWidgets import QApplication

from window import Window
from keyboard_handler import KeyboardHandler


def main():
    app = QApplication(sys.argv)
    window = Window()
    keyboard_hangler = KeyboardHandler(window)
    keyboard_hangler.start()
    app.exec_()

if __name__ == '__main__':
    main()
