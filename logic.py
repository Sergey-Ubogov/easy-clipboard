import clipboard
from keyboard import press, release
import helpers.mouse_helper as mouse_helper


def read_clipboard(window):
    data = clipboard.paste()
    with window.lock:
        window.add_signal.emit(data)

def get_pos_hint(window):
    x, y = mouse_helper.get_mousepos()
    screen_width, screen_height = mouse_helper.get_screen_size()

    #при первом открытии flameGrometry выдает 479, 639 почему то, потом нормуль
    #flame_geometry = window.frameGeometry()
    hint_width = 256#flame_geometry.width()
    hint_height = 192#flame_geometry.height()
    #print(x, y, hint_height, hint_width, screen_width, screen_height)
    if (y + hint_height > screen_height):
        y -= hint_height
    if (x + hint_width > screen_width):
        x -= hint_width

    return x, y

def show_buffer(window):
    x, y = get_pos_hint(window)
    print(x, y)
    window.render_signal.emit(x, y)


def imitate_paste(text: str):
    clipboard.copy(text)
    press('ctrl')
    press('v')
    release('v')
    release('ctrl')
