from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication)

class Window(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.resize(self.width, self.height)
        self.setWindowTitle('EasyClipboard')
        self.labels = []
    
    def show_window(self, x, y, _buffer):
        self.move(x, y)
        self.show()

    def show_minimized(self):
        self.showMinimized()

    def show_normal(self, _buffer):
        self.showNormal()
        buffer_length = len(_buffer)
        labels_length = len(self.labels)
        if (buffer_length > labels_length):
            print(buffer_length, labels_length)
            for i in range(buffer_length - labels_length):
                label = QLabel(self)
                label.setText(_buffer[i + labels_length])
                label.move(10, 20*i)
                print('move')
                self.labels.append(label)


    