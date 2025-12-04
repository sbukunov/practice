import time
import requests
import psutil
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton


class SystemInfo(QtCore.QThread):
    systemInfoReceived = Signal(list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay=1
        self.__status= True

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while self.__status:
            cpu_value = psutil.cpu_percent(interval=0.5)
            ram_value = psutil.virtual_memory().percent
            self.systemInfoReceived.emit([cpu_value,ram_value])
            time.sleep(self.delay)

    def stop(self):
        self.__status = False



class WeatherHandler(QtCore.QThread):
    weatherUpdateStarted = Signal()
    weatherInfoReceived = Signal(dict)
    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 1
        self.__status = True

    def setDelay(self, delay) -> None:
        self.__delay = delay

    def stop(self):
        self.__status = False

    def run(self) -> None:
        if self.__status is None:
            self.__status=True

        while self.__status:
            self.weatherUpdateStarted.emit()
            response = requests.get(self.__api_url)
            data = response.json()
            self.weatherInfoReceived.emit(data)
            time.sleep(self.__delay)


class SystemInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.initThread()
    def initUI(self) -> None:
        layoutMain=QVBoxLayout()

        layoutMain.addWidget(QLabel("Задержка:"))
        self.delayEditLine = QLineEdit()
        self.delayEditLine.setText("1")
        layoutMain.addWidget(self.delayEditLine)

        self.cpuLabel = QLabel("CPU INFO")
        self.ramLabel = QLabel("RAM INFO")
        layoutMain.addWidget(self.cpuLabel)
        layoutMain.addWidget(self.ramLabel)

        self.delayEditLine.textChanged.connect(self.changeValueDelay)
        self.setLayout(layoutMain)

    def initThread(self):
        self.mainThread = SystemInfo()
        self.mainThread.systemInfoReceived.connect(self.updateInfo)
        try:
            self.mainThread.delay = int(self.delayEditLine.text())
        except:
            self.mainThread.delay = 1

        self.mainThread.start()

    def updateInfo(self,info):
        self.cpuLabel.setText(f'CPU INFO {info[0]} %')
        self.ramLabel.setText(f'RAM INFO {info[1]} %')

    def changeValueDelay(self,value):
        if value and value.isdigit():
            self.mainThread.delay = int(value)

    def stopThread(self):
        self.mainThread.stop()
        self.mainThread.quit()
        self.mainThread.wait()


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
        self.weatherInfoLabel.setText(f"Температура: {temperature} °C")

    def closeEvent(self, event):
        if self.isRunning:
            self.stopWeatherThread()
        event.accept()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.sys = SystemInfoWidget()
        self.weather = WeatherInfoWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.sys)
        layout.addWidget(self.weather)

        btn = QPushButton("Exit")
        btn.clicked.connect(self.close)
        layout.addWidget(btn)

        self.setLayout(layout)

    def closeEvent(self, event):
        self.sys.stopThread()
        if self.weather.isRunning:
            self.weather.stopWeatherThread()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = MainWindow()
    w.show()
    app.exec()
