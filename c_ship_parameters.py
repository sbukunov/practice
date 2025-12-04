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
        self.lbl_1 = QLabel("Температура на борту")
        self.lbl_2 = QLabel("Разгерметизация")
        self.lbl_3 = QLabel("Бак №1")
        self.lbl_4 = QLabel("Бак №2")
        self.lbl_5 = QLabel("Бак №3")
        self.lbl_1.setFixedSize(150, 25)
        self.lbl_2.setFixedSize(150, 25)
        self.lbl_3.setFixedSize(150, 25)
        self.lbl_4.setFixedSize(150, 25)
        self.lbl_5.setFixedSize(150, 25)
        self.lbl_1.setStyleSheet('color: white; font: 500 12pt Times New Roman; border-color: red')
        self.lbl_2.setStyleSheet('color: white; font: 500 12pt Times New Roman;')
        self.lbl_3.setStyleSheet('color: white; font: 500 12pt Times New Roman;')
        self.lbl_4.setStyleSheet('color: white; font: 500 12pt Times New Roman;')
        self.lbl_5.setStyleSheet('color: white; font: 500 12pt Times New Roman;')
        self.line_1 = QLineEdit("22 C")
        self.line_2 = QLineEdit("Отсутствует")
        self.line_3 = QLineEdit("Норма")
        self.line_4 = QLineEdit("Норма")
        self.line_5 = QLineEdit("Норма")
        self.line_1.setStyleSheet('color: yellow; font: 500 10pt Times New Roman')
        self.line_2.setStyleSheet('color: lightgreen; font: 500 10pt Times New Roman')
        self.line_3.setStyleSheet('color: lightgreen; font: 500 10pt Times New Roman')
        self.line_4.setStyleSheet('color: lightgreen; font: 500 10pt Times New Roman')
        self.line_5.setStyleSheet('color: lightgreen; font: 500 10pt Times New Roman')
        #Размещение виджетов
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()
        layout_3 = QHBoxLayout()
        layout_4 = QHBoxLayout()
        layout_5 = QHBoxLayout()
        layout_1.addWidget(self.lbl_1)
        layout_1.addWidget(self.line_1)
        layout_2.addWidget(self.lbl_2)
        layout_2.addWidget(self.line_2)
        layout_3.addWidget(self.lbl_3)
        layout_3.addWidget(self.line_3)
        layout_4.addWidget(self.lbl_4)
        layout_4.addWidget(self.line_4)
        layout_5.addWidget(self.lbl_5)
        layout_5.addWidget(self.line_5)
        layout = QVBoxLayout()
        layout.addLayout(layout_1)
        layout.addLayout(layout_2)
        layout.addLayout(layout_3)
        layout.addLayout(layout_4)
        layout.addLayout(layout_5)
        self.setLayout(layout)
        # Заголовок окна
        self.setWindowTitle("Параметры корабля")
        self.setStyleSheet('background-color:grey')

app = QApplication()
window = Window()
window.show()

app.exec()