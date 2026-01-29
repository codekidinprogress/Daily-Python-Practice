import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLineEdit, QPushButton,
    QVBoxLayout, QGridLayout
)
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(400, 200, 350, 450)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setPlaceholderText("0")
        self.display.setObjectName("display")

        grid = QGridLayout()
        grid.setSpacing(10)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row, col = 0, 0
        for btn_text in buttons:
            button = QPushButton(btn_text)
            button.clicked.connect(self.onButtonClick)
            grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_btn = QPushButton("Clear")
        clear_btn.setObjectName("clear")
        clear_btn.clicked.connect(self.clearDisplay)
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid)
        main_layout.addWidget(clear_btn)
        central_widget.setLayout(main_layout)

        self.setStyleSheet("""
            QLineEdit#display {
                font-size: 22px;
                padding: 15px;
                border: 2px solid gray;
                border-radius: 8px;
            }

            QPushButton {
                font-size: 16px;
                padding: 15px;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #e0e0e0;
            }

            QPushButton#clear {
                background-color: hsl(0, 100%, 64%);
                font-size: 18px;
            }

            QPushButton#clear:hover {
                background-color: hsl(0, 100%, 84%);
            }
        """)

    def onButtonClick(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                expression = self.display.text()
                result = eval(expression)
                self.display.setText(f"{expression} = {result}")
            except:
                self.display.setText("Error")
        else:
        
            if "=" in self.display.text():
                self.display.clear()
            self.display.setText(self.display.text() + text)

    def clearDisplay(self):
        self.display.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
