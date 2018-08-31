import keyboard
from PyQt5.QtCore import QThread

from window import Window
from logic import show_buffer, read_clipboard


class KeyboardHandler(QThread):
    def __init__(self, window: Window):
        QThread.__init__(self)
        self.window = window

    def ctrl_c_handler(self):
        read_clipboard(self.window)

    def ctrl_shift_v_handler(self):
        show_buffer(self.window)

    def __del__(self):
        self.wait()

    def run(self):
        keyboard.add_hotkey('ctrl+c', self.ctrl_c_handler) 
        keyboard.add_hotkey('ctrl+shift+v', self.ctrl_shift_v_handler, suppress=True)
        keyboard.wait()
