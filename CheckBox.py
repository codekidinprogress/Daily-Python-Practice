import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Food Preference")
        self.setGeometry(700, 300, 500, 300)
        self.checkbox = QCheckBox("I like fast food 🍔", self)
        self.checkbox.setGeometry(50, 50, 400, 50)
        self.checkbox.setStyleSheet("font-size: 24px; font-family: Arial;")
        self.checkbox.stateChanged.connect(self.checkbox_changed)
        self.result_label = QLabel("Select your preference", self)
        self.result_label.setGeometry(50, 120, 400, 50)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 20px;")

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            self.result_label.setText("You like fast food 😋")
        else:
            self.result_label.setText("You prefer healthy food 🥗")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
