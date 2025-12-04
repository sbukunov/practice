from PySide6 import QtWidgets, QtCore
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lcd_modes = {
            "hex": QtWidgets.QLCDNumber.Mode.Hex,
            "dec": QtWidgets.QLCDNumber.Mode.Dec,
            "oct": QtWidgets.QLCDNumber.Mode.Oct,
            "bin": QtWidgets.QLCDNumber.Mode.Bin,
        }
        self.initUi()
        self.initWidgets()
        self.__loadSettings()

    def initUi(self):
        fileUi = QFile("ui\\d_eventfilter_settings_form.ui")
        fileUi.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(fileUi, self)
        fileUi.close()

    def initWidgets(self):
        self.dial = self.ui.findChild(QtWidgets.QDial, "dial")
        self.lcd = self.ui.findChild(QtWidgets.QLCDNumber, "lcdNumber")
        self.slider = self.ui.findChild(QtWidgets.QSlider, "horizontalSlider")
        self.cb = self.ui.findChild(QtWidgets.QComboBox, "comboBox")

        self.dial.setRange(0, 100)
        self.dial.valueChanged.connect(self.onValueChanged)
        self.dial.installEventFilter(self)

        self.lcd.display(14)
        self.lcd.setMinimumHeight(60)

        self.slider.setRange(0, 100)
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider.installEventFilter(self)
        self.slider.valueChanged.connect(self.onValueChanged)

        self.cb.addItems(list(self.lcd_modes.keys()))
        self.cb.currentTextChanged.connect(self.onModeChanged)

    def __loadSettings(self):
        settings = QtCore.QSettings("SimpleTextEditApp")
        mode = settings.value("lcd_mode", "dec")
        value = int(settings.value("lcd_value", 0))
        if mode in self.lcd_modes:
            self.cb.setCurrentText(mode)
            self.lcd.setMode(self.lcd_modes[mode])
        self.dial.setValue(value)
        self.slider.setValue(value)
        self.lcd.display(value)

    def __saveSettings(self):
        settings = QtCore.QSettings("SimpleTextEditApp")
        settings.setValue("lcd_mode", self.cb.currentText())
        settings.setValue("lcd_value", self.dial.value())

    def onValueChanged(self, value):
        self.dial.blockSignals(True)
        self.slider.blockSignals(True)

        self.dial.setValue(value)
        self.slider.setValue(value)

        self.dial.blockSignals(False)
        self.slider.blockSignals(False)

        mode = self.cb.currentText()
        newValue = self.formatValue(value, mode)
        self.lcd.display(newValue)
        print("Новое значение: ", newValue)
        self.__saveSettings()

    def onModeChanged(self, mode):
        if mode in self.lcd_modes:
            self.lcd.setMode(self.lcd_modes[mode])
            value = self.dial.value()
            newValue = self.formatValue(value, mode)
            self.lcd.display(newValue)
            self.__saveSettings()

    def formatValue(self, value, mode):
        match mode:
            case "hex":
                return f"{value:X}"
            case "oct":
                return f"{value:o}"
            case "bin":
                return f"{value:b}"
            case "dec":
                return str(value)

    def closeEvent(self, event):
        self.__saveSettings()
        super().closeEvent(event)

    def eventFilter(self, watched, event):
        if (watched == self.dial or watched == self.slider) and event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == QtCore.Qt.Key.Key_Minus:
                self.dial.setValue(self.dial.value() - 1)
            elif event.key() == QtCore.Qt.Key.Key_Plus:
                self.dial.setValue(self.dial.value() + 1)
        return super().eventFilter(watched, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec()
