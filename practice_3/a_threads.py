import time
import requests
import psutil
from PySide6 import QtCore
from PySide6.QtCore import Signal


class SystemInfo(QtCore.QThread):
    systemInfoReceived = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = 1
        self.__status = True

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while self.__status:
            cpu_value = psutil.cpu_percent(interval=0.5)
            ram_value = psutil.virtual_memory().percent
            self.systemInfoReceived.emit([cpu_value, ram_value])
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
            self.__status = True

        while self.__status:
            self.weatherUpdateStarted.emit()
            response = requests.get(self.__api_url)
            data = response.json()
            self.weatherInfoReceived.emit(data)
            time.sleep(self.__delay)
