from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide6.QtWidgets import QPushButton, QLabel, QLineEdit, QGroupBox
from PySide6 import QtWidgets


class Window(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        #Создание виджетов
        self.lbl_1 = QLabel("Фамилия")
        self.lbl_2 = QLabel("Имя")
        self.lbl_3 = QLabel("Отчество")
        self.lbl_4 = QLabel("Телефон")
        self.lbl_1.setFixedSize(75, 25)
        self.lbl_2.setFixedSize(75, 25)
        self.lbl_3.setFixedSize(75, 25)
        self.lbl_4.setFixedSize(75, 25)

        self.lbl_1.setStyleSheet('color: white; font: 500 12pt Times New Roman; border-color: red')
        self.lbl_2.setStyleSheet('color: white; font: 500 12pt Times New Roman;')
        self.lbl_3.setStyleSheet('color: white; font: 500 12pt Times New Roman;')
        self.lbl_4.setStyleSheet('color: white; font: 500 12pt Times New Roman;')
        self.line_1 = QLineEdit()
        self.line_1.setPlaceholderText("Введите Вашу фамилию")
        self.line_2 = QLineEdit()
        self.line_2.setPlaceholderText("Введите Ваше имя")
        self.line_3 = QLineEdit()
        self.line_3.setPlaceholderText("Введите Ваше отчество")
        self.line_4 = QLineEdit()
        self.line_4.setPlaceholderText("Введите Ваш номер телефона")
        self.line_1.setFixedSize(200, 25)
        self.line_2.setFixedSize(200, 25)
        self.line_3.setFixedSize(200, 25)
        self.line_4.setFixedSize(200, 25)
        self.line_1.setStyleSheet('color: yellow; font: 500 10pt Times New Roman')
        self.line_2.setStyleSheet('color: yellow; font: 500 10pt Times New Roman')
        self.line_3.setStyleSheet('color: yellow; font: 500 10pt Times New Roman')
        self.line_4.setStyleSheet('color: yellow; font: 500 10pt Times New Roman')
        #Размещение виджетов
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()
        layout_3 = QHBoxLayout()
        layout_4 = QHBoxLayout()
        layout_1.addWidget(self.lbl_1)
        layout_1.addWidget(self.line_1)
        layout_2.addWidget(self.lbl_2)
        layout_2.addWidget(self.line_2)
        layout_3.addWidget(self.lbl_3)
        layout_3.addWidget(self.line_3)
        layout_4.addWidget(self.lbl_4)
        layout_4.addWidget(self.line_4)
        layout = QVBoxLayout()
        layout.addLayout(layout_1)
        layout.addLayout(layout_2)
        layout.addLayout(layout_3)
        layout.addLayout(layout_4)
        self.setLayout(layout)
        # Заголовок окна
        self.setWindowTitle("Профиль")
        self.setStyleSheet('background-color:black')

app = QApplication()
window = Window()
window.show()

app.exec()