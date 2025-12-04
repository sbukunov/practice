from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide6.QtWidgets import QPushButton, QLabel, QLineEdit


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        # TODO Вызовите метод для инициализации интерфейса

    def initUi(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        self.labelLogin = QLabel("Логин")  # TODO Создайте виджет QLabel с текстом "Логин"
        self.labelRegistration = QLabel("Регистрация") # TODO Создайте виджет QLabel с текстом "Регистрация"

        self.lineEditLogin = QLineEdit()  # TODO создайте виджет QLineEdit
        self.lineEditLogin.setPlaceholderText("Введите логин")  # TODO добавьте placeholderText "Введите логин" с помощью метода .setPlaceholderText()
        self.lineEditPassword = QLineEdit()  # TODO создайте виджет QLineEdit
        self.lineEditPassword.setPlaceholderText("Введите пароль")  # TODO добавьте placeholderText "Введите пароль"
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)  # TODO установите ограничение видимости вводимых знаков с помощью метода .setEchoMode()

        self.pushButtonLogin = QPushButton()  # TODO создайте виджет QPushButton
        self.pushButtonLogin.setText("Войти")  # TODO установите текст "Войти" с помощью метода setText()

        self.pushButtonRegistration = QPushButton()  # TODO создайте виджет QPushButton
        self.pushButtonRegistration.setText("Регистрация")  # TODO установите текст "Регистрация" с помощью метода setText()

        layoutLogin = QHBoxLayout()  # TODO Создайте QHBoxLayout
        layoutLogin.addWidget(self.labelLogin)  # TODO с помощью метода .addWidget() добавьте labelLogin
        layoutLogin.addWidget(self.lineEditLogin) # TODO с помощью метода .addWidget() добавьте self.lineEditLogin

        layoutPassword = QHBoxLayout()  # TODO Создайте QHBoxLayout
        layoutPassword.addWidget(self.labelRegistration) # TODO с помощью метода .addWidget() добавьте labelRegistration
        layoutPassword.addWidget(self.lineEditPassword) # TODO с помощью метода .addWidget() добавьте self.lineEditPassword

        layoutButtons = QHBoxLayout()  # TODO Создайте QHBoxLayout
        layoutButtons.addWidget(self.pushButtonLogin)  # TODO с помощью метода .addWidget() добавьте self.pushButtonLogin
        layoutButtons.addWidget(self.pushButtonRegistration)  # TODO с помощью метода .addWidget() добавьте self.pushButtonRegistration

        layoutMain = QVBoxLayout()  # TODO Создайте QVBoxLayout
        layoutMain.addLayout(layoutLogin)  # TODO с помощью метода .addLayout() добавьте layoutLogin
        layoutMain.addLayout(layoutPassword)  # TODO с помощью метода .addLayout() добавьте layoutPassword
        layoutMain.addLayout(layoutButtons)  # TODO с помощью метода .addLayout() добавьте layoutButtons

        self.setLayout(layoutMain)  # TODO с помощью метода setLayout установите layoutMain на основной виджет


if __name__ == "__main__":
    app = QApplication()

    window = Window()
    window.show()

    app.exec()
