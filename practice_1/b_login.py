from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit

class Window(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        self.lbl_log = QLabel("Login")
        self.line_log = QLineEdit()
        self.lbl_pas = QLabel("Password")
        self.line_pas = QLineEdit()
        self.lbl_log.setFixedSize(50, 25)
        self.lbl_pas.setFixedSize(50, 25)
        self.btn_quit = QPushButton("Войти")
        self.btn_quit.setStyleSheet('background-color: grey; color: white;')
        self.line_log.setStyleSheet('background-color: grey; color: white;')
        self.line_pas.setStyleSheet('background-color: grey; color: white;')
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()
        layout_1.addWidget(self.lbl_log)
        layout_1.addWidget(self.line_log)
        layout_2.addWidget(self.lbl_pas)
        layout_2.addWidget(self.line_pas)
        layout = QVBoxLayout()
        layout.addLayout(layout_1)
        layout.addLayout(layout_2)
        layout.addWidget(self.btn_quit)
        self.setLayout(layout)
        self.setWindowTitle("Login")
        self.setStyleSheet('background-color: black; color: white;')
        self.resize(300, 100)

app = QApplication()
window = Window()
window.show()

app.exec()