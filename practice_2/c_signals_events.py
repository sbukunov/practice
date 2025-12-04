"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущий основной монитор
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

from PySide6.QtWidgets import QApplication, QWidget

from ui.c_signals_events_form import Ui_Form  # Импортируем класс формы
class Window(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()

    def initUi(self):
        # Создание "прокси" переменной для работы с формой
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Состояния окна")

    def initSignals(self):
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLTClicked)
        self.ui.pushButtonRT.clicked.connect(self.onPushButtonRTClicked)
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonCenterClicked)
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLBClicked)
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonRBClicked)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoordsClicked)
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)

    # slots --------------------------------------------------------------
    def onPushButtonLTClicked(self) -> None:
        screen = self.screen().geometry()
        self.move(screen.left(), screen.top())
    def onPushButtonRTClicked(self) -> None:
        screen = self.screen().geometry()
        self.move(screen.right() - self.width(), screen.top())
    def onPushButtonCenterClicked(self) -> None:
        screen = self.screen().geometry()
        self.setGeometry((screen.width() - self.width()) // 2,
                         (screen.height() - self.height()) // 2,
                         self.width(), self.height())

    def onPushButtonLBClicked(self) -> None:
        screen = self.screen().geometry()
        self.setGeometry(screen.left(), screen.bottom() - self.frameSize().height(), self.width(), self.height())

    def onPushButtonRBClicked(self) -> None:
        screen = self.screen().geometry()
        self.setGeometry(screen.right() - self.frameSize().width(), screen.bottom() - self.frameSize().height(),
                         self.width(), self.height())

    def onPushButtonMoveCoordsClicked(self) -> None:
        screen = self.screen().geometry()
        self.move(screen.left() + self.ui.spinBoxX.value(), screen.top() + self.ui.spinBoxY.value())

    def onPushButtonGetDataClicked(self) -> None:
        screen = self.screen().geometry()
        self.ui.plainTextEdit.setPlainText(f"Размеры окна: {self.size().width()} x {self.size().height()}\n"
                                        f"Координаты окна: X = {self.x()}, Y = {self.y()}")

if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()

    app.exec()
