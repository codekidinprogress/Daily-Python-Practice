import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
    QFormLayout, QHBoxLayout, QTextEdit, QComboBox, QDateEdit)
from PyQt5.QtCore import QDate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Application Form")
        self.setGeometry(300, 150, 650, 600)
        self.initUI()
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.fullname = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()
        self.course = QLineEdit()
        self.age = QLineEdit()

        self.gender = QComboBox()
        self.gender.addItems(["Select", "Male", "Female", "Other"])

        self.dob = QDateEdit()
        self.dob.setCalendarPopup(True)
        self.dob.setDate(QDate.currentDate())

        self.guardian = QLineEdit()
        self.skills = QTextEdit()
        self.address = QTextEdit()

        for widget in [
            self.fullname, self.email, self.phone, self.course,
            self.age, self.guardian
        ]:
            widget.setObjectName("input")

        self.skills.setObjectName("textArea")
        self.address.setObjectName("textArea")
        self.gender.setObjectName("combo")
        self.dob.setObjectName("input")

        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Full Name:"), self.fullname)
        form_layout.addRow(QLabel("Email:"), self.email)
        form_layout.addRow(QLabel("Phone Number:"), self.phone)
        form_layout.addRow(QLabel("Course Applied:"), self.course)
        form_layout.addRow(QLabel("Age:"), self.age)
        form_layout.addRow(QLabel("Gender:"), self.gender)
        form_layout.addRow(QLabel("Date of Birth:"), self.dob)
        form_layout.addRow(QLabel("Guardian Name:"), self.guardian)
        form_layout.addRow(QLabel("Skills:"), self.skills)
        form_layout.addRow(QLabel("Address:"), self.address)

        self.submit_btn = QPushButton("Submit")
        self.reset_btn = QPushButton("Reset")

        self.submit_btn.setObjectName("submit")
        self.reset_btn.setObjectName("reset")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_btn)
        button_layout.addWidget(self.reset_btn)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        central_widget.setLayout(main_layout)

        self.reset_btn.clicked.connect(self.clearFields)

        self.setStyleSheet("""
            QLabel {
                font-size: 15px;
                font-family: Arial;
            }

            QLineEdit#input, QDateEdit#input {
                font-size: 15px;
                padding: 8px;
                border: 2px solid gray;
                border-radius: 8px;
            }

            QTextEdit#textArea {
                font-size: 14px;
                border: 2px solid gray;
                border-radius: 8px;
            }

            QComboBox#combo {
                font-size: 15px;
                padding: 6px;
                border-radius: 8px;
            }

            QPushButton {
                font-size: 18px;
                padding: 10px 35px;
                border-radius: 12px;
            }

            QPushButton#submit {
                background-color: hsl(122, 100%, 64%);
            }

            QPushButton#submit:hover {
                background-color: hsl(122, 100%, 84%);
            }

            QPushButton#reset {
                background-color: hsl(0, 100%, 64%);
            }

            QPushButton#reset:hover {
                background-color: hsl(0, 100%, 84%);
            }
        """)

    def clearFields(self):
        self.fullname.clear()
        self.email.clear()
        self.phone.clear()
        self.course.clear()
        self.age.clear()
        self.guardian.clear()
        self.skills.clear()
        self.address.clear()
        self.gender.setCurrentIndex(0)
        self.dob.setDate(QDate.currentDate())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())