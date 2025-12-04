from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton
from aTreads import *


class WeatherInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.weatherThread = None
        self.isRunning = False

    def initUI(self) -> None:
        layoutMain = QVBoxLayout()

        layoutMain.addWidget(QLabel("Широта:"))
        self.widthEditLine = QLineEdit()
        self.widthEditLine.setText("59.9386")
        layoutMain.addWidget(self.widthEditLine)

        layoutMain.addWidget(QLabel("Долгота:"))
        self.longEditLine = QLineEdit()
        self.longEditLine.setText("30.3141")
        layoutMain.addWidget(self.longEditLine)

        layoutMain.addWidget(QLabel("Задержка:"))
        self.delayEditLine = QLineEdit()
        self.delayEditLine.setText("1")
        layoutMain.addWidget(self.delayEditLine)

        self.startButton = QPushButton("Start weather")
        layoutMain.addWidget(self.startButton)

        self.weatherInfoLabel = QLabel("Здесь будет отображена погода")
        layoutMain.addWidget(self.weatherInfoLabel)

        self.startButton.clicked.connect(self.stateWeatherThread)
        self.setLayout(layoutMain)

    def stateWeatherThread(self):
        if not self.isRunning:
            self.startWeatherThread()
        else:
            self.stopWeatherThread()

    def startWeatherThread(self):
        width = float(self.widthEditLine.text())
        long = float(self.longEditLine.text())
        delay = int(self.delayEditLine.text())

        self.widthEditLine.setEnabled(False)
        self.longEditLine.setEnabled(False)
        self.delayEditLine.setEnabled(False)

        self.weatherThread = WeatherHandler(width, long)
        self.weatherThread.setDelay(delay)
        self.weatherThread.weatherInfoReceived.connect(self.onWeatherInfoReceived)

        self.weatherThread.start()
        self.isRunning = True
        self.startButton.setText("Stop")

    def stopWeatherThread(self):
        if self.weatherThread and self.weatherThread.isRunning():
            self.weatherThread.stop()
            self.weatherThread.quit()
            self.weatherThread.wait()

        self.widthEditLine.setEnabled(True)
        self.longEditLine.setEnabled(True)
        self.delayEditLine.setEnabled(True)

        self.isRunning = False
        self.startButton.setText("Start weather")

    def onWeatherInfoReceived(self, weather):
        temperature = weather['current_weather']['temperature']
        self.weatherInfoLabel.setText(f"Температура: {temperature}°C")

    def closeEvent(self, event):
        if self.isRunning:
            self.stopWeatherThread()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = WeatherInfoWidget()
    window.show()
    app.exec()