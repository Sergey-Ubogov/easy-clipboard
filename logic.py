import clipboard
from keyboard import press, release
#import win32gui


def read_clipboard(window):
    data = clipboard.paste()
    with window.lock:
        window.add_signal.emit(data)


def show_buffer(window):
    x,y = win32gui.GetCursorInfo()[2]
    window.render_signal.emit(x, y)


def imitate_paste(text: str):
    clipboard.copy(text)
    press('ctrl')
    press('v')
    release('v')
    release('ctrl')
