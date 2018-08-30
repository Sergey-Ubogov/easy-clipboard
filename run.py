import keyboard
import win32gui
import sys
from gui import Window
import clipboard
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread

class KeyboardHandler(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        keyboard.add_hotkey('ctrl+c', read_clipboard) 
        keyboard.add_hotkey('ctrl+shift+v', show_buffer, suppress=True)
        keyboard.wait()

WINDOW = None
BUFFER = []

def read_clipboard():
    data = clipboard.paste()
    BUFFER.append(data)

def show_buffer():
    WINDOW.show_normal(BUFFER)

def start_gui():
    global WINDOW
    app = QApplication(sys.argv)
    WINDOW = Window(250, 200)

    flags, hcursor, (x,y) = win32gui.GetCursorInfo()
    WINDOW.show_window(x, y, BUFFER)
    WINDOW.show_minimized()
    app.exec_()

def main():
    keyboard_hangler = KeyboardHandler()
    keyboard_hangler.start()
    print('main')
    start_gui()
    print('exit')

if __name__ == '__main__':
    main()