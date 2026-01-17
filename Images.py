import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 500, 500)

        pixmap = QPixmap("pic.jpeg")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
